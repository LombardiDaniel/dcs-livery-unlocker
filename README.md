[![tag](https://img.shields.io/github/v/release/LombardiDaniel/dcs-livery-unlocker?include_prereleases&style=for-the-badge)](https://github.com/LombardiDaniel/Reddbot/releases)

# DCS Livery Unlocker
Simple script to unlock all skins from all nations in DCS: World.

## Table of Contents

-   [Download and Usage](#download-and-usage)
    -   [Download](#download)
    -   [Usage](#Usage)
-   [License](#license)
-   [Acknowledgments](#acknowledgments)

## Download and Usage

### Download

You can get the latest executable from [releases](https://github.com/LombardiDaniel/dcs-livery-unlocker/releases). Or from the UserFiles: [https://www.digitalcombatsimulator.com/en/files/3318254/]

### Usage

Just point the app to your `DCS install folder` and to the `Saved Games/DCS` folder on your computer. Note: do NOT point it to `Saved Games`, point it to `Saved Games/DCS.openbeta` or `Saved Games/DCS`. (Changed from previous versions)

## License

This project is under the MIT license - see the file [LICENSE.md](LICENSE.md) for details.

## Acknowledgments

* Hat tip to anyone whose code was used
* Thanks to [Atom](https://atom.io/) for being an awesome text editor

Create executable (from `src` folder):
```sh
pyinstaller --onefile --icon=logo.ico main.py
```
