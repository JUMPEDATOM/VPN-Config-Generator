
# VPN-Config-Generator

The VPN Config Generator is a Python program that automates the process of creating free VPN accounts. It utilizes the Selenium library to interact with https://panel.gozargah.one/# the VPN provider's website, automating the account creation process. One of the key features of this program is the ability to bypass reCAPTCHA, ensuring a smooth and seamless account generation experience.





## Features

- Automated VPN account creation: The program automates the entire process of generating VPN accounts, eliminating the need for manual intervention.
- Bypass reCAPTCHA challenges: By leveraging Selenium's browser automation capabilities, the program can bypass reCAPTCHA challenges commonly encountered during account creation.
- Free VPN accounts: The generator focuses on creating free VPN accounts, providing users with a convenient solution for accessing VPN services.




## Optimizations

One optimization in this script is the ability to bypass reCAPTCHA challenges. To overcome this problem, a solution is implemented where a sound from the reCAPTCHA challenge is selected. Then, the sound is converted to text using Python language, and the obtained text is automatically filled into the requested field.


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`BROWSER_PATH` `{your browser PATH}`

`BROWSER_DRIVER` `{your downloaded browser driver PATH}`


## Run Locally

Clone the project

```bash
  git clone https://github.com/JUMPEDATOM/VPN-Config-Generator.git
```

Go to the project directory

```bash
  cd VPN-Config-Generator-master
```

Install dependencies

```bash
   pip install -r requirements.txt
```

Run script

```bash
  python configGenerator.py
```


## License

[MIT](https://choosealicense.com/licenses/mit/)

