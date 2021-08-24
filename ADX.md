# Setting up Azure Data Explorer

In this section, we set up our Azure environment and configure the resources. Please note that ADX can ingest data from muliple sources (including streams). In this example we will ingest from a storage account.

## Step 1: Create Resources

1. Create a resource group under your Azure subscription.
2. Inside the newly created Resource Group, create the following resources:
   2.1. Azure Data Explorer ([click to create](https://ms.portal.azure.com/#create/Microsoft.AzureKusto))
   2.2. Storage Account ([click to create](https://ms.portal.azure.com/#create/Microsoft.StorageAccount-ARM))
   ![Azure Resources](/images/azure-resources.png)

3. Create a new Private container named: _rawdata_ in the Storage Account.
   ![Create Raw Data Container](/images/create-raw-container.png)

## Step 2: Upload Data

1. Upload the generated data to the newly created _rawdata_ container.
   ![Upload Raw Data](/images/upload-raw-data.png)
