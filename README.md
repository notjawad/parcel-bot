# ParcelBot 🚚

ParcelBot allows tracking your packages in a Discord server using the [Parcel App](https://parcelapp.net/) for iOS & macOS devices.



## Usage

This bot sends a request to the Parcel App's web app with a user's account token. To get your token you will need to sign in at [web.parcelapp.net](https://web.parcelapp.net/). After logging in follow the below steps:

1. `Ctrl + Shift + I` to bring up developer tools
2. Go to the `Network` tab & refresh the page
3. Click on `data.php?callback=...`
4. Click on `Headers` tab and scroll down until you see `Request Headers`
5. Finally, your account token will be stored in the `cookie` header as `account_token`

You then need to supply that to the bot in order to login:
```
$auth token
```
See `help` command for more.

## Preview
![Preview](https://i.gyazo.com/ce771d1d26ba137fa81d90c4582e27cc.png)

## TODO

- [ ] Add delivery notifications in DM.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
