# stackspot-ai-security-action-poc
StackSpot AI Security Action POC

## Usage

```yaml
- uses: GuillaumeFalourd/stackspot-ai-security-action-poc@main
  id: run
  with:
    CLIENT_ID: ${{ secrets.CLIENT_ID }}
    CLIENT_KEY: ${{ secrets.CLIENT_KEY }}
    ACCOUNT_SLUG: stackspot
    QC_SLUG: sast-rqc
```
