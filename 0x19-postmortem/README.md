# 0x19. Postmortem


## Issue Summary

On 27 September at 14:00 UTC, 100% of the page was inactive for a total of 30 min, the service was restored at 14:30 pm UTC. Users experienced a response with a 500 status code (internal server error). When we did the review on the server where the page was hosted, we could find that the main cause of the interruption was a typographical error of a single letter in a `.php` file, it was written as a `.phpp` file.


## Timeline

- **14:00** : After deploying wordpress, and a response was made to the server to check the correct operation where it was found that the response was 500 status code.

- **14:05** : Active processes were verified using `ps auxf`.

- **14:14** : It was followed up with the `strace` command and we could see that there was a problem with the file `/var /www/html/wp-config.php`.

- **14:17** : The website was curled to reveal a fatal error, a missing file `/var/www/html/wp-includes/class-wp-locale.phpp` required in `/var/www/html/wp-settings.php`. The nonexistent `.phpp` extension indicated a potential typographical error.

- **14:20** : With the ls command the content of `/var/www/html/wp-includes/` was listed and the existence of the file `/ var/www/html/wp-settings.php` was confirmed.

- **14:22**: Fixed using `sed` command in php config file.

- **14:25** : A puppet manifest was used with the following command `sudo sed -i s/class-wp-locale.phpp/class-wp-locale.php/g/var/www/html/wp-settings.php`.

- **14:27** : The website was tested to verify proper operation.

- **14:30** : The website worked correctly and was ready.


## Root cause and resolution:

The main cause of this interruption was a typo in the php file `/var/www/html/wp-settings.php` in which the file `/var/www/html/wp-includes/class-wp-locale.phpp` was required. The `.phpp` extension was a typo, meant to be `.php` . Since `/var/www/html/wp-includes/class-wp-locale.phpp` did not exist and was required, a fatal error was thrown that prevented the content from being served. That caused the complete crash of the server, a puppet file was used to make the complete and efficient correction, the service was restored in 30 min.


## Corrective and preventative measures:

To prevent large-scale problems like this from occurring in the future, the code should be deployed to the servers after doing certain tests to verify that it works properly. Some things to consider for the future include: developing an enterprise-wide test protocol, setting up isolated Docker containers for testing purposes and adding in-server memory monitoring.
