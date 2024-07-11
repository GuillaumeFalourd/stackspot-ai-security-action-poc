# stackspot-ai-security-action-poc

[![Action Test Ubuntu](https://github.com/GuillaumeFalourd/stackspot-ai-security-action-poc/actions/workflows/action-test-ubuntu.yaml/badge.svg)](https://github.com/GuillaumeFalourd/stackspot-ai-security-action-poc/actions/workflows/action-test-ubuntu.yaml) [![Daily action Test](https://github.com/GuillaumeFalourd/stackspot-ai-security-action-poc/actions/workflows/daily-action-test.yaml/badge.svg)](https://github.com/GuillaumeFalourd/stackspot-ai-security-action-poc/actions/workflows/daily-action-test.yaml)

StackSpot AI Security Action POC

This action identify vulnerabilities (SAST check) using StackSpot AI Remote Quick Command concept.

It returns a list of vulnerabilities for each file, following the structure below:
```
[
  {
    "title": "<TITLE>",
    "severiity": "<SEVERITY>",
    "correction": "<CORRECTION>",
    "lines": "<LINES>"
  }
]
```
_Note: This action solely identifies files that have changed for events such as pull_request*, push, merge_group, release, etc (potentially the same events referred [here](https://github.com/tj-actions/changed-files?tab=readme-ov-file#examples-)). However, it doesn't detect pending uncommitted changes created during the workflow execution._

## Usage

```yaml
on:
  pull_request:

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

permissions: # mandatory to add comment on PR
  issues: write
  pull-requests: write

jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: GuillaumeFalourd/stackspot-ai-security-action-poc@main
        id: run
        with:
          CLIENT_ID: ${{ secrets.CLIENT_ID }}
          CLIENT_KEY: ${{ secrets.CLIENT_KEY }}
          CLIENT_REALM: stackspot
          QC_SLUG: sast-rqc
```

## ▶️ Action Inputs

Field | Mandatory | Default Value | Observation
------------ | ------------  | ------------- | -------------
**CLIENT_ID** | YES | N/A | [StackSpot](https://stackspot.com/en/settings/access-token) Client ID.
**CLIENT_KEY** | YES | N/A |[StackSpot](https://stackspot.com/en/settings/access-token) Client KEY.
**CLIENT_REALM** | YES | N/A |[StackSpot](https://stackspot.com/en/settings/access-token) Client Realm.
**QC_SLUG** | YES | N/A | [StackSpot Remote Quick Command reference](https://ai.stackspot.com/docs/pt-br/quick-commands/create-remote-qc)

## Remote Quick Commands available

### SAST

![](https://github.com/GuillaumeFalourd/stackspot-ai-security-action-poc/assets/22433243/935c79b1-e86a-4738-ac0d-ba3be90d2dbb)

#### Output

Pipeline
![](https://github.com/GuillaumeFalourd/stackspot-ai-security-action-poc/assets/22433243/b6fee6a9-c968-4a5e-91dc-d65d3b393286)

PR comment
<img width="766" alt="Screenshot 2024-07-11 at 08 20 09" src="https://github.com/GuillaumeFalourd/stackspot-ai-security-action-poc/assets/22433243/04487d1a-ba30-4c31-a78b-8df0e24395b4">


### DAST

TODO

## Roadmap tasks

- [ ] DAST RQC.
- [x] Add comment on PR.
- [x] Generate vulnerability report ([example](https://github.com/GuillaumeFalourd/stackspot-ai-security-action-poc/pull/1#issuecomment-2208860075))
- [ ] Add an action configuration file.

## Observations

To run any StackSpot AI remote quick command, please check [https://github.com/GuillaumeFalourd/stackspot-ai-rqc](https://github.com/GuillaumeFalourd/stackspot-ai-rqc).
