# i18n-processing

### Usage

1. Locate default `messages.properties` file for program to process into template.
2. Run `create-template.py` to create a template to send to a customer using an exsting i18n properties file
2. Send `template.csv` to client to fill out required languages.
3. Run `export-template-to-properties.py` to export the returned template to it's component individual language `.properties` files

>**Note:** Any properties which are not found in the definitions.json file will be included in the template using their backend name rather than a readable name. 
>
>   Additional properties can be added to the `definitions.json` file so that they get formatted correctly in the future
