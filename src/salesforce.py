import logging
from config.config import Config
from simple_salesforce import Salesforce, SalesforceLogin


class SalesforceAPI:
    def __init__(self):
        """
        Constructor method to initialize Salesforce instance and logger.
        """
        self.sf = self.get_salesforce_instance()  # Initialize Salesforce instance
        self.logger = logging.getLogger(__name__)

    def get_salesforce_instance(self):
        """
        Method to authenticate and initialize Salesforce instance.
        Returns:
            Salesforce instance.
        """
        try:
            session_id, instance = SalesforceLogin(
                username=Config.SALESFORCE_USERNAME,
                password=Config.SALESFORCE_PASSWORD,
                security_token=Config.SALESFORCE_SECURITY_TOKEN,
            )
            print(
                f"INFO: initiated Salesforce instance with {Config.SALESFORCE_USERNAME}"
            )
            return Salesforce(instance=instance, session_id=session_id)
        except Exception as e:
            print(f"Error while initiating Salesforce instance: {str(e)}")

    def fetch_data(self, query):
        """
        Method to fetch data from Salesforce using a SOQL query.
        Args:
            query (str): SOQL query to fetch data.
        Returns:
            Query result containing fetched data.
        """
        try:
            query_records = self.sf.query_all(query)
            self.logger.info("Fetched data from Salesforce")
            return query_records
        except Exception as e:
            self.logger.error(f"Error while fetching data from Salesforce: {str(e)}")

    def delete_records(self, record_ids, table_name):
        """
        Method to delete records from Salesforce.
        Args:
            record_ids (list): List of record IDs to be deleted.
            table_name (str): Name of the Salesforce object from which records are to be deleted.
        """
        try:
            self.delete_associated_records(record_ids, ["Entitlement", "Case", "Opportunity"])

            for id in record_ids:
                self.sf.__getattr__(table_name).delete(id)
            self.logger.info("Deleted data from Salesforce")
        except Exception as e:
            self.logger.error(f"Error while deleting data from Salesforce: {str(e)}")
