# stackspot-ai-security-action-poc

StackSpot AI Security Action POC working on all operating system.

## Usage

```yaml
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

![](https://github.com/GuillaumeFalourd/stackspot-ai-security-action-poc/assets/22433243/01269c32-5614-436d-ae63-486a7fa6b1f5)

### DAST

TODO

## Roadmap tasks

- [ ] DAST RQC.
- [ ] Add comment on PR.
- [ ] Generate vulnerability report.
- [ ] Add an action configuration file.
