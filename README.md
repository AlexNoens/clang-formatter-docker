# griffin-tools-fromat
Repo for holding for formatting scripts for the various file types relevant to project Griffin. Will contain both the information needed by CircleCi to run format checks on firmware, and the scripts for developers to run.

## Supported file types

Currently this repo only handles c/cpp files.
## Using this repo

The executable is found in the clang/dist foler. You can simply run the excecuatble form your project root to run a format on all of your c/cpp files. Your project's root will need a `.clang-format` file to be able to use specific configurations.
