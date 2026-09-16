# lcom-plugins

This repository is the working home for Learning.com context used by ChatGPT.

Its current primary deliverable is the **`lcom-business-context` Skill**, which provides curated business knowledge such as ontology definitions, glossary content, and business rules. The repository is intentionally structured so that additional **Skills**, **Plugins**, and **MCP servers** can be added later.

## Repository purpose

Use this repository to:

- develop and maintain Learning.com business knowledge for AI use;
- create and test ontology, glossary, prompts, and supporting business context;
- maintain scripts and other tooling used to prepare or validate that knowledge;
- publish finished Skills, Plugins, and MCP components in locations intended for ChatGPT.

## Repository structure

```text
lcom-business-context/
├── README.md
├── workbench/
├── plugins/
├── mcp/
└── .agents/
```

### `workbench/`

`workbench/` is the main working area for humans.

Keep all development and maintenance material here, including:

- raw source material;
- ontology and business-knowledge drafts;
- prompts;
- Python maintenance scripts;
- test questions and expected results;
- notes and design documents;
- intermediate or generated files that are not part of a final ChatGPT component.

Example:

```text
workbench/
├── raw/
├── drafts/
├── prompts/
├── scripts/
├── tests/
└── docs/
```

Files in `workbench/` are not considered final ChatGPT deliverables.

### `plugins/`

Reserved for final Plugin content intended for ChatGPT.

The current `lcom-business-context` Skill belongs under the appropriate Plugin structure here. Additional Skills or Plugins may be added later.

Only reviewed, ready-to-use content should be copied or promoted from `workbench/` into `plugins/`.

### `mcp/`

Reserved for MCP servers and related production-ready MCP components intended for ChatGPT use.

Development notes, experiments, prompts, and helper scripts should remain in `workbench/` until they are ready to become part of an MCP implementation.

### `.agents/`

Reserved for ChatGPT/OpenAI agent configuration and Plugin marketplace metadata.

Do not use this folder for general documentation, drafts, or maintenance files.

## Working principle

The repository follows a simple separation:

```text
workbench/
    = where humans create, investigate, draft, test, and maintain

plugins/
mcp/
.agents/
    = where finalized ChatGPT-facing components live
```

All new work should begin in `workbench/`.

Once content or code is reviewed and ready for use, move or copy the final version into the appropriate ChatGPT-facing destination:

- Skill or Plugin content → `plugins/`
- MCP server content → `mcp/`
- ChatGPT/OpenAI configuration or marketplace metadata → `.agents/`

## Current scope

The repository currently focuses on the **`lcom-business-context` Skill**, including business ontology and curated business knowledge.

The structure is designed to support future expansion without requiring a new repository for every capability. Additional Skills, Plugins, MCP servers, and supporting AI components can be added as the project grows.

## Maintenance guideline

When editing this repository:

1. Make changes in `workbench/`.
2. Review and test the result.
3. Promote only finalized content to `plugins/`, `mcp/`, or `.agents/`.
4. Keep ChatGPT-facing folders clean and free of drafts, raw material, and temporary files.
