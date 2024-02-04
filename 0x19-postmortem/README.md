Postmortem: Apache Container Debugging

Issue Summary:
Duration: 15 minutes
Start Time: 2023-11-20 09:00 AM (GMT)
End Time: 2023-11-20 09:15 AM (GMT)
Impact: Docker container for Apache not returning expected content on port 8080.

Root Cause:
The Apache container failed to return the correct page due to a misconfiguration in the Apache server settings.

Timeline:
9:00 AM: Started Docker container using ‘docker run -p 8080:80 -d -it holbertonschool/265-0’.
9:02 AM: Checked container status using docker ps and observed it was running.
9:03 AM: Attempted to access the Apache server on port 8080 using curl 0:8080 and received an empty reply.
9:05 AM: Logged into the container using docker exec -it <container_id> /bin/bash to investigate the Apache configuration.
9:07 AM: Examined the Apache server configuration files in /etc/apache2/sites-available/000-default.conf and identified an incorrect DocumentRoot setting.
9:10 AM: Modified the DocumentRoot to the correct directory path using vim /etc/apache2/sites-available/000-default.conf.
9:12 AM: Restarted the Apache service within the container using service apache2 restart.
9:15 AM: Confirmed the issue was resolved by curling port 8080, receiving the expected "Hello Holberton" page.





Root Cause and Resolution:

Root Cause:

The misconfiguration in the Apache server's DocumentRoot setting resulted in the server not serving the expected content.


Resolution:

The issue was resolved by correcting the DocumentRoot configuration in the Apache server settings and restarting the Apache service within the container.

Corrective and Preventative Measures:

To Improve/Fix:
Implement automated checks during container startup to validate Apache server configuration.
Regularly review and update container configurations to align with application requirements

Tasks to Address the Issue:

Add a startup script to the Dockerfile that checks and logs the Apache server configuration status during container initialization.
Create documentation for container maintainers outlining the best practices for configuring Apache within Docker containers.

Conclusion:

The Apache container issue was promptly addressed by identifying and correcting the misconfiguration in the server settings. By implementing automated checks and maintaining clear documentation on best practices, we aim to prevent similar configuration issues in the future. This incident highlights the importance of regular configuration reviews and testing during container development and deployment.
