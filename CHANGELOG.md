# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html) (at least it tries).

## [Unreleased]
- Simple methods like Select
- Find a way to avoid resetting the generator when looping through the Enumerable
- Type conversions
- Aggregate functions
- Performance tests
- Extend python syntax with query keywords
- Examples and use cases

## [0.0.1] - 2022-05-04
### Added
- Enumerable class
- Select method
- Where method

## [0.0.2] - 2022-05-05
### Added
- IEnumerable, an interface defining every method used in order for autocompletion to work but unable to be instanciated and the methods can't be called
- Extends, a decorator to extend a class method
- Conversion to list

### Modified
- Moved to their own folder Select and Where method in "query"