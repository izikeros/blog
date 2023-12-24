---
Category: note
Date: '2023-04-11'
Modified: '2023-07-12'
Slug: how-to-deploy-freshrss-in-the-cloud-for-free-on-azure
Status: published
Tags: rss, freshrss, cloud-deploy, free-deploy, azure
Title: How to Deploy FreshRSS in the Cloud for Free on Azure?
todo: verify the steps
---

FreshRSS is a free and open-source RSS feed aggregator that allows you to easily follow your favorite websites and blogs in one place. By deploying FreshRSS in the cloud, you can access your feeds from anywhere and enjoy the benefits of cloud computing, such as scalability, reliability, and cost-effectiveness. Microsoft Azure is a popular cloud platform that offers a wide range of services for building, deploying, and managing applications in the cloud. In this tutorial, we'll show you how to deploy FreshRSS in the cloud for free on Azure.

<!-- MarkdownTOC levels="2,3" autolink="true" autoanchor="true" -->

- [Prerequisites:](#prerequisites)
- [Step-by-step guide](#step-by-step-guide)
  - [Step 1: Create a new Azure web app](#step-1-create-a-new-azure-web-app)
  - [Step 2: Configure your web app](#step-2-configure-your-web-app)
  - [Step 3: Deploy FreshRSS](#step-3-deploy-freshrss)
  - [Step 4: Configure SSL (optional)](#step-4-configure-ssl-optional)

<!-- /MarkdownTOC -->

<a id="prerequisites"></a>
## Prerequisites:

-   A Microsoft Azure account
-   A basic understanding of Azure services and concepts
-   A web browser
-   An SSH client (optional)

<a id="step-by-step-guide"></a>
## Step-by-step guide
<a id="step-1-create-a-new-azure-web-app"></a>
### Step 1: Create a new Azure web app

The first step is to create a new Azure web app, which will host your FreshRSS installation. Follow these steps to create a new web app:

1.  Log in to the Azure portal ([https://portal.azure.com](https://portal.azure.com/)) using your Azure account credentials.

2.  Click on the "Create a resource" button in the left-hand menu and search for "Web App".

3.  Select the "Web App" service and click on the "Create" button.

4.  Fill in the required details for your web app, such as the name, subscription, resource group, and runtime stack.

5.  Choose the "Free" pricing tier, which provides up to 10 web, mobile, or API apps with shared compute resources and 1 GB storage per app.

6.  Click on the "Review + create" button to review your settings and then click on the "Create" button to create your web app.

7.  Wait for the deployment to complete, which may take a few minutes.


<a id="step-2-configure-your-web-app"></a>
### Step 2: Configure your web app

The next step is to configure your web app with the necessary settings and dependencies. Follow these steps to configure your web app:

1.  Navigate to your web app in the Azure portal and click on the "Configuration" tab.

2.  Under the "General settings" section, set the "Linux container" option to "On".

3.  Under the "Stack settings" section, set the "Runtime stack" option to "PHP 7.3".

4.  Under the "Application settings" section, add the following key-value pairs:

    -   Key: WEBSITE_TIME_ZONE, Value: Your timezone (e.g., "America/Los_Angeles")
    -   Key: WEBSITE_AUTH_ENABLED, Value: False
    -   Key: WEBSITE_NODE_DEFAULT_VERSION, Value: 10.14.2
5.  Click on the "Save" button to save your changes.


<a id="step-3-deploy-freshrss"></a>
### Step 3: Deploy FreshRSS

The next step is to deploy FreshRSS to your web app. Follow these steps to deploy FreshRSS:

1.  Download the latest version of FreshRSS from the official website ([https://freshrss.org](https://freshrss.org/)) and extract the files to a local directory.

2.  Open a command prompt or terminal window and navigate to the local directory where you extracted the FreshRSS files.

3.  Use the following command to create a ZIP archive of the FreshRSS files:


    `zip -r freshrss.zip .`

4.  Return to the Azure portal and navigate to your web app.

5.  Click on the "Deployment Center" tab and select the "Local Git" option.

6.  Follow the on-screen instructions to create a new deployment user and download the deployment credentials.

7.  Use the following commands to add the Azure Git remote to your local Git repository and push your changes to the Azure web app:

    csharpCopy code

    `git remote add azure <deployment-endpoint> git push azure master`


8.  When prompted, enter the deployment username and password that you created earlier.

9.  Wait for the deployment to complete, which may take a few minutes.

10.  Once the deployment is complete, open a web browser and navigate to your web app's URL to access FreshRSS. You should see the FreshRSS installation page.

11.  Follow the on-screen instructions to complete the FreshRSS installation. Make sure to set the database type to "SQLite" and the database path to "/home/site/wwwroot/data/freshrss.db".

12.  Once the installation is complete, you should be able to access FreshRSS and start adding your favorite feeds.


<a id="step-4-configure-ssl-optional"></a>
### Step 4: Configure SSL (optional)

If you want to secure your FreshRSS installation with SSL, you can do so by configuring a custom domain and adding an SSL certificate. Follow these steps to configure SSL:

1.  Purchase a custom domain from a domain registrar, such as GoDaddy or Namecheap.

2.  Navigate to your web app in the Azure portal and click on the "Custom domains" tab.

3.  Add your custom domain and follow the on-screen instructions to configure DNS settings.

4.  Once your domain is configured, navigate to the "SSL certificates" tab and click on the "Create App Service Managed Certificate" button.

5.  Follow the on-screen instructions to create a new SSL certificate for your custom domain.

6.  Once the certificate is created, navigate back to the "Custom domains" tab and click on the "Add binding" button.

7.  Select your custom domain and the newly created SSL certificate and click on the "Add binding" button.

8.  Wait for the SSL certificate to be provisioned, which may take a few minutes.

9.  Once the SSL certificate is provisioned, you should be able to access FreshRSS securely using your custom domain.

X::[[fresh_rss_deploy_on_GCP]]
up::[[MOC_RSS]]
