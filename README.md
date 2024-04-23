# stackspot-ai-security-action-poc

StackSpot AI Security Action POC working on all operating system.

This action identify vulnerabilities (SAST check) on files updated compared to the repository `main` branch.

_Note: This action solely identifies files that have changed for events such as pull_request*, push, merge_group, release, ... However, it doesn't detect pending uncommitted changes created during the workflow execution._

## Usage

```yaml
name: Action Test Ubuntu

on:
  pull_request:

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

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

![](https://github.com/GuillaumeFalourd/stackspot-ai-security-action-poc/assets/22433243/aef6cbcd-0ed4-49ef-973e-6b24bd2e950b)

#### Output

![](https://github.com/GuillaumeFalourd/stackspot-ai-security-action-poc/assets/22433243/b6fee6a9-c968-4a5e-91dc-d65d3b393286)

### DAST

TODO

## Roadmap tasks

- [ ] DAST RQC.
- [ ] Add comment on PR.
- [ ] Generate vulnerability report.
- [ ] Add an action configuration file.
