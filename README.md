<div align="center">
<h6>Utility</h6>
<h1>🖥️ MobaXterm 🖥️</h1>

<br />

<p>Utility for MobaXterm</p>

<br />
<br />

</div>

<div align="center">

<!-- prettier-ignore-start -->
[![Version][github-version-img]][github-version-uri] [![Build Status][github-build-img]][github-build-uri] [![Downloads][github-downloads-img]][github-downloads-uri] [![Size][github-size-img]][github-size-img] [![Last Commit][github-commit-img]][github-commit-img] [![Contributors][contribs-all-img]](#contributors-)
<!-- prettier-ignore-end -->

</div>

<br />

---

<br />

- [About](#about)
- [Usage](#usage)
  - [Binary](#binary)
  - [Script](#script)
- [Options](#options)
- [Arguments](#arguments)
- [Build](#build)
- [Contributors ✨](#contributors-)

<br />

---

<br />

## About
This is a utility for MobaXterm which is to be utilized for educational purposes only.

<br />

---

<br />

## Usage
To use this utility pick one of the executing methods below:

- [Binary](#binary)
- [Python Script](#script)

<br />
<br />

### Binary
Utilize the following command to run the utility using the binary on the releases page.

```bash
mobaxtgen_cli.exe [OPTIONS] <name> <version> <users>
```

<br />

```bash
$ mobaxtgen_cli.exe "Aetherx" 24.2 4
```

<br />

Returns the following:
```ini
Created File .............: X:\XmobaTerms\Custom.mxtpro
Username .................: Aetherx
License Enc ..............: 2sWCtwDItoDM0o3e6tGfrp3e7pnf6tGerh3a4tG
License Str ..............: 1#Aetherx|232#4#233262#0#0#0#
Version ..................: 24.2
Users ....................: 4
```

<br />
<br />
<br />

### Script
This method is for users who wish to run the utility with Python 3.

<br />

```bash
mobaxtgen_cli.py [OPTIONS] <name> <version> <users>
```

<br />

```bash
$ mobaxtgen_cli.exe -s "Aetherx" 24.2 4
```

<br />

Output:

```ini
2sWCtwDItoDM0o3e6tGfrp3e7pnf6tGerh3a4tG
```

<br />

---

<br />

## Options
When running this utility, you can also utilize the following options:

<br />

| Arg       | Desc                      |
| --------- | ------------------------- |
| `-s`      | Output simple result      |
| `-h`      | Help information          |

<br />

---

<br />

## Arguments
The following parameters can be passed to specify required information the utility needs from you to complete generation:

<br />

|                       | Desc                                | State       | Default |
| --------------------- | ----------------------------------- | ----------- | ------- |
| **`user`**            | Username for license                | _required_  |         |
| **`version`**         | Version license to be generated for | _optional_  | 24.2    |
| **`users`**           | Number of users allowed for license | _optional_  | 1       |

<br />

---

<br />

## Build

- Download [IronPython 3.x](https://github.com/IronLanguages/ironpython3/releases) and install to `x:\IronPython\3.x.x`
- Copy `mobaxtgen_cli.py` and place in same directory where `ipy.exe` exists
- Copy `verinfo.py` and place in same directory where `mobaxtgen_cli.py` exists
- Open `verinfo.py` and modify the data:
- Open Windows Terminal / Command Prompt and execute `pip install pyinstaller`
- Execute the following command in terminal:

```bash
pyinstaller -Fwc mobaxtgen_cli.py --version-file "verinfo.py" -i "moba.ico" --workpath "tmp" --distpath "x:\IronPython\3.x.x\dist\mobaxtgen_cli.exe"
```

<br />

> [!WARNING]
> If you do not add `c` to the list of arguments, the exe will output nothing to console.

<br />

- New .exe will be placed in `x:\IronPython\3.x.x\dist\mobaxtgen_cli.exe`

<br />

---

<br />

## Contributors ✨
We are always looking for contributors. If you feel that you can provide something useful to Gistr, then we'd love to review your suggestion. Before submitting your contribution, please review the following resources:

- [Pull Request Procedure](.github/PULL_REQUEST_TEMPLATE.md)
- [Contributor Policy](CONTRIBUTING.md)

<br />

Want to help but can't write code?
- Review [active questions by our community](https://github.com/Aetherinox/mobaxterm-utility-py/labels/help%20wanted) and answer the ones you know.

<br />

The following people have helped get this project going:

<br />

<div align="center">

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![Contributors][contribs-all-img]](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top"><a href="https://gitlab.com/Aetherinox"><img src="https://avatars.githubusercontent.com/u/118329232?v=4?s=40" width="80px;" alt="Aetherinox"/><br /><sub><b>Aetherinox</b></sub></a><br /><a href="https://github.com/Aetherinox/mobaxterm-utility-py/commits?author=Aetherinox" title="Code">💻</a> <a href="#projectManagement-Aetherinox" title="Project Management">📆</a> <a href="#fundingFinding-Aetherinox" title="Funding Finding">🔍</a></td>
    </tr>
  </tbody>
</table>
</div>
<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

<br />
<br />

<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->

<!-- BADGE > GENERAL -->
  [general-npmjs-uri]: https://npmjs.com
  [general-nodejs-uri]: https://nodejs.org
  [general-npmtrends-uri]: http://npmtrends.com/mobaxterm-utility-py

<!-- BADGE > VERSION > GITHUB -->
  [github-version-img]: https://img.shields.io/github/v/tag/Aetherinox/mobaxterm-utility-py?logo=GitHub&label=Version&color=ba5225
  [github-version-uri]: https://github.com/Aetherinox/mobaxterm-utility-py/releases

<!-- BADGE > VERSION > NPMJS -->
  [npm-version-img]: https://img.shields.io/npm/v/mobaxterm-utility-py?logo=npm&label=Version&color=ba5225
  [npm-version-uri]: https://npmjs.com/package/mobaxterm-utility-py

<!-- BADGE > VERSION > PYPI -->
  [pypi-version-img]: https://img.shields.io/pypi/v/mobaxterm-utility-py-plugin
  [pypi-version-uri]: https://pypi.org/project/mobaxterm-utility-py-plugin/

<!-- BADGE > LICENSE > MIT -->
  [license-mit-img]: https://img.shields.io/badge/MIT-FFF?logo=creativecommons&logoColor=FFFFFF&label=License&color=9d29a0
  [license-mit-uri]: https://github.com/Aetherinox/mobaxterm-utility-py/blob/main/LICENSE

<!-- BADGE > GITHUB > DOWNLOAD COUNT -->
  [github-downloads-img]: https://img.shields.io/github/downloads/Aetherinox/mobaxterm-utility-py/total?logo=github&logoColor=FFFFFF&label=Downloads&color=376892
  [github-downloads-uri]: https://github.com/Aetherinox/mobaxterm-utility-py/releases

<!-- BADGE > NPMJS > DOWNLOAD COUNT -->
  [npmjs-downloads-img]: https://img.shields.io/npm/dw/%40aetherinox%2Fmkdocs-link-embeds?logo=npm&&label=Downloads&color=376892
  [npmjs-downloads-uri]: https://npmjs.com/package/mobaxterm-utility-py

<!-- BADGE > GITHUB > DOWNLOAD SIZE -->
  [github-size-img]: https://img.shields.io/github/repo-size/Aetherinox/mobaxterm-utility-py?logo=github&label=Size&color=59702a
  [github-size-uri]: https://github.com/Aetherinox/mobaxterm-utility-py/releases

<!-- BADGE > NPMJS > DOWNLOAD SIZE -->
  [npmjs-size-img]: https://img.shields.io/npm/unpacked-size/mobaxterm-utility-py/latest?logo=npm&label=Size&color=59702a
  [npmjs-size-uri]: https://npmjs.com/package/mobaxterm-utility-py

<!-- BADGE > CODECOV > COVERAGE -->
  [codecov-coverage-img]: https://img.shields.io/codecov/c/github/Aetherinox/mobaxterm-utility-py?token=MPAVASGIOG&logo=codecov&logoColor=FFFFFF&label=Coverage&color=354b9e
  [codecov-coverage-uri]: https://codecov.io/github/Aetherinox/mobaxterm-utility-py

<!-- BADGE > ALL CONTRIBUTORS -->
  [contribs-all-img]: https://img.shields.io/github/all-contributors/Aetherinox/mobaxterm-utility-py?logo=contributorcovenant&color=de1f6f&label=contributors
  [contribs-all-uri]: https://github.com/all-contributors/all-contributors

<!-- BADGE > GITHUB > BUILD > NPM -->
  [github-build-img]: https://img.shields.io/github/actions/workflow/status/Aetherinox/mobaxterm-utility-py/release.yml?logo=github&logoColor=FFFFFF&label=Build&color=%23278b30
  [github-build-uri]: https://github.com/Aetherinox/mobaxterm-utility-py/actions/workflows/release.yml

<!-- BADGE > GITHUB > BUILD > Pypi -->
  [github-build-pypi-img]: https://img.shields.io/github/actions/workflow/status/Aetherinox/mobaxterm-utility-py/release-pypi.yml?logo=github&logoColor=FFFFFF&label=Build&color=%23278b30
  [github-build-pypi-uri]: https://github.com/Aetherinox/mobaxterm-utility-py/actions/workflows/pypi-release.yml

<!-- BADGE > GITHUB > TESTS -->
  [github-tests-img]: https://img.shields.io/github/actions/workflow/status/Aetherinox/mobaxterm-utility-py/npm-tests.yml?logo=github&label=Tests&color=2c6488
  [github-tests-uri]: https://github.com/Aetherinox/mobaxterm-utility-py/actions/workflows/npm-tests.yml

<!-- BADGE > GITHUB > COMMIT -->
  [github-commit-img]: https://img.shields.io/github/last-commit/Aetherinox/mobaxterm-utility-py?logo=conventionalcommits&logoColor=FFFFFF&label=Last%20Commit&color=313131
  [github-commit-uri]: https://github.com/Aetherinox/mobaxterm-utility-py/commits/main/

<!-- prettier-ignore-end -->
<!-- markdownlint-restore -->
