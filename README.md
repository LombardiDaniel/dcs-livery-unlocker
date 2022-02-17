[![tag](https://img.shields.io/github/v/release/LombardiDaniel/dcs-livery-unlocker?include_prereleases&style=for-the-badge)](https://github.com/LombardiDaniel/Reddbot/releases)

# DCS Livery Unlocker
Simple script to unlock all skins from all nations in DCS: World.

## Table of Contents

-   [Download and Usage](#download-and-usage)
    -   [Download](#download)
    -   [Usage](#Usage)
-   [Changelog](#changelog)
-   [License](#license)
-   [Acknowledgments](#acknowledgments)

## Download and Usage

### Download

You can get the latest executable from [releases](https://github.com/LombardiDaniel/dcs-livery-unlocker/releases). Or from the UserFiles: https://www.digitalcombatsimulator.com/en/files/3318254/

### Usage

Just point the app to your `DCS install folder` and to the `Saved Games/DCS` folder on your computer. Note: do NOT point it to `Saved Games`, point it to `Saved Games/DCS.openbeta` or `Saved Games/DCS`. (Changed from previous versions)

## Changelog
Changelog:
- `1.0`: Initial Release.
- `1.1`: Changed how the script reads files (some people had errors on SavedGames).
- `1.2`: Helicopters and every other vehicle in the game (including ground vehicles).
- `1.2.1`: Internal build is different, uses [glob](https://docs.python.org/3/library/glob.html) package (simpler code), also fixed a bug where some skins (due to lua file structure) would be ignored.

## License

This project is under the MIT license - see the file [LICENSE.md](LICENSE.md) for details.

## Acknowledgments

* Hat tip to anyone whose code was used
* Thanks to [Atom](https://atom.io/) for being an awesome text editor

Create executable (from `src` folder):
```sh
pyinstaller --clean --onefile --icon='logo.ico' main.py
```
