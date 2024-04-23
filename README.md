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
**ACCOUNT_SLUG** | YES | N/A |[StackSpot](https://stackspot.com/en/settings/access-token) Client Realm.
**QC_SLUG** | YES | N/A | [StackSpot Remote Quick Command reference](https://ai.stackspot.com/docs/pt-br/quick-commands/create-remote-qc)
