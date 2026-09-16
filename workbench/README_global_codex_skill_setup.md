# Global Codex Skill Setup on Windows

This guide configures a Codex skill so it can be used across all repositories, the Codex VS Code extension, and Codex Desktop, while keeping the real skill files in an existing project repository.

The approach is:

- keep the canonical skill files in the existing repository;
- create the global Codex skills directory under the Windows user profile;
- create a Windows junction from the global skills directory to the repository's `skill` folder.

This avoids duplicating or manually synchronizing the skill files.

## Step 1 — Check the Windows home directory

Run in PowerShell:

```powershell
$HOME
```

Expected output should be your Windows user directory, for example:

```text
C:\Users\KDrogaieva
```

## Step 2 — Verify whether `.agents` already exists

Run in PowerShell:

```powershell
Test-Path "$HOME\.agents"
```

Expected result:

```text
True
```

if the `.agents` directory already exists.

If the result is:

```text
False
```

the directory does not exist yet and must be created in the next step.

## Step 3 — Create the global Codex skills directory

Run in PowerShell:

```powershell
New-Item -ItemType Directory -Force -Path "$HOME\.agents\skills"
```

Expected output should show the new `skills` directory under:

```text
C:\Users\<your-user>\.agents
```

Verify that the directory exists:

```powershell
Test-Path "$HOME\.agents\skills"
```

Expected result:

```text
True
```

## Step 4 — Verify the existing skill folder

From the project root, run:

```powershell
Get-ChildItem ".\skill"
```

Expected output should include:

```text
SKILL.md
knowledge
ontology
```

Verify that `SKILL.md` exists:

```powershell
Test-Path ".\skill\SKILL.md"
```

Expected result:

```text
True
```

For this project, the full skill path is:

```text
C:\Users\KDrogaieva\OneDrive - Learning.com\Development\lcom-business-context\skill
```

## Step 5 — Create the global link to the skill

Create a junction from the global Codex skills directory to the existing project skill folder.

Run in PowerShell:

```powershell
New-Item `
  -ItemType Junction `
  -Path "$HOME\.agents\skills\learning-business-knowledge" `
  -Target "C:\Users\KDrogaieva\OneDrive - Learning.com\Development\lcom-business-context\skill"
```

Expected output should show:

```text
C:\Users\KDrogaieva\.agents\skills\learning-business-knowledge
```

Verify that the junction exposes the skill contents:

```powershell
Get-ChildItem "$HOME\.agents\skills\learning-business-knowledge"
```

Expected contents:

```text
SKILL.md
knowledge
ontology
```

The skill remains physically stored in the project repository, while Codex can access it globally through:

```text
C:\Users\KDrogaieva\.agents\skills\learning-business-knowledge
```

## Step 6 — Verify the `SKILL.md` header

Run in PowerShell:

```powershell
Get-Content "$HOME\.agents\skills\learning-business-knowledge\SKILL.md" -TotalCount 20
```

The file should start with YAML front matter containing at least:

```markdown
---
name: learning-com-business-knowledge
description: >
  ...
---
```

Verify that:

- `SKILL.md` starts with `---`
- a `name` field is present
- a `description` field is present
- the YAML block ends with `---`

For this skill, the recognized skill name is:

```text
learning-com-business-knowledge
```

The description should clearly explain when Codex should use the skill, especially for Learning.com-specific business terminology, reporting definitions, relationships, and business rules.

## Step 7 — Verify the skill in Codex VS Code

Restart VS Code or the Codex extension so it reloads the available skills.

In the Codex chat input, run:

```text
/skills
```

Expected result: the skill should appear in the available skills list, for example:

```text
learning-com-business-knowledge
```

with a description similar to:

```text
Learning.com terminology, reporting definitions, and business rules
```

If the skill appears, the global user-level skill setup is working correctly in the Codex VS Code extension.

## Step 8 — Test explicit use of the skill in Codex VS Code

In the Codex chat input, explicitly invoke the skill:

```text
$learning-com-business-knowledge
```

Then ask a question that should be answered from the Learning.com business knowledge files, for example:

```text
$learning-com-business-knowledge

What is an LCom Customer?
```

Expected result:

- Codex accepts the skill reference.
- Codex uses the skill's `SKILL.md` instructions.
- Codex reads the relevant supporting knowledge files when needed.
- The answer follows Learning.com-specific definitions rather than generic business assumptions.

If the answer matches the documented Learning.com business knowledge, explicit skill invocation is working correctly.

`$learning-com-business-knowledge` is mainly useful when you want to force the skill to be used, such as for testing, troubleshooting, or ambiguous questions. In normal use, Codex can select the skill automatically based on its description.

## Step 9 — Verify the skill in Codex Desktop

Open the ChatGPT desktop application and switch to the Codex view.

In a Codex chat, run:

```text
/skills
```

Expected result: the skill should appear in the available skills list:

```text
learning-com-business-knowledge
```

If it appears, Codex Desktop can access the same global user-level skill.

No additional copy of the skill is required.

## Final structure

The canonical skill remains in the repository:

```text
C:\Users\KDrogaieva\OneDrive - Learning.com\Development\lcom-business-context\skill
├── SKILL.md
├── knowledge
└── ontology
```

The global Codex location contains a junction to that folder:

```text
C:\Users\KDrogaieva\.agents\skills\learning-business-knowledge
```

This allows the same skill to be used from:

- Codex VS Code
- Codex Desktop
- other repositories opened by Codex
