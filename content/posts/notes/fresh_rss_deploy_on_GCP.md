---
Title: How to deploy FreshRSS in the cloud for free on GCP?
Slug: how-to-deploy-freshrss-in-the-cloud-for-free-on-gcp
Date: 2023-04-11
Modified: 2023-04-11
Status: published
Tags: rss, freshrss, cloud-deploy, free-deploy, gcp, google-cloud-platform, google
Category: note
todo: verify the steps
---


To deploy FreshRSS in the cloud for free on Google Cloud Platform (GCP), you can follow these steps:

1.  Create a new project on GCP and enable billing. FreshRSS requires a web server and a database, and GCP provides free usage limits for these services for a limited time. You will need to provide billing information to verify your account and enable these services.
    
2.  Launch a Compute Engine instance. FreshRSS can run on any Linux-based server, so you can choose an instance that meets your needs. For this example, we'll use a micro instance with Debian 10.
    
3.  Connect to the instance using SSH. You can use the SSH button in the GCP Console or connect from your terminal using the external IP address.
    
4.  Install the necessary packages. Run the following command to update the package index and install the required packages:
    
```sh
sudo apt update
sudo apt install apache2 mariadb-server php7.3 php7.3-mysql php7.3-curl php7.3-xml
```
    
5.  Configure the database. Follow these steps to create a new database and user for FreshRSS:
    
```sh
sudo mysql -u root

CREATE DATABASE freshrss;
GRANT ALL PRIVILEGES ON freshrss.* TO 'freshrssuser'@'localhost' IDENTIFIED BY 'password';
FLUSH PRIVILEGES;
EXIT;

```
    
6.  Download and install FreshRSS. Run the following commands to download the latest version of FreshRSS and extract it to the web root:
    
```sh
cd /var/www/html
sudo wget https://github.com/FreshRSS/FreshRSS/archive/master.tar.gz
sudo tar -xzf master.tar.gz --strip-components=1
sudo chown -R www-data:www-data .
```
    
7.  Configure the web server. Edit the default Apache configuration file to enable URL rewriting:
    
```sh
sudo nano /etc/apache2/sites-enabled/000-default.conf

```
    
    Add the following lines inside the `<VirtualHost>` block:
    
```xml
<Directory /var/www/html>
    AllowOverride All
</Directory>

```
    
8.  Restart the web server. Run the following command to apply the changes:
    
```sh
sudo systemctl restart apache2
```
    
9.  Complete the FreshRSS setup. Open your web browser and navigate to the external IP address of your instance. Follow the on-screen instructions to configure FreshRSS.
    

Congratulations, you have successfully deployed FreshRSS in the cloud for free on GCP!

X::[[freshrss_deploy_on_azure]]
up::[[MOC_RSS]]
