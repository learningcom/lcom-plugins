# Upload and Share `lcom-business-context` as a ChatGPT Workspace Skill

> Verified against current OpenAI workspace Skill documentation on September 15, 2026.

## Before you start

You should already have a ZIP file with this structure:

```text
lcom-business-context.zip
├── SKILL.md
├── ontology/
│   ├── ...
└── knowledge/
    ├── ...
```

`SKILL.md` should be at the root of the ZIP file.

---

## 1. Sign in to the correct ChatGPT account

1. Open ChatGPT in your browser.
2. Sign in using your company ChatGPT account.
3. Make sure you are working inside the Learning.com company workspace, not your personal ChatGPT workspace.

If your account belongs to more than one workspace, switch to the company workspace before continuing.

---

## 2. Open Skills

1. In the ChatGPT left sidebar, select **Plugins**.
2. Open the **Plugin Directory**.
3. Select the **Skills** tab.

You should see sections such as:

- **Installed**
- **Created by me**
- **Shared with me**
- **Shared by Learning.com** or a similarly named workspace section

---

## 3. Upload the ZIP file

1. On the **Skills** page, select **Create**.
2. Select **Upload from your computer**.
3. Choose:

```text
lcom-business-context.zip
```

4. Wait for ChatGPT to scan the Skill.

Most Skills become available after the scan completes.

The Skill may instead show:

- **Needs Review** — review the information ChatGPT provides before continuing.
- **Blocked** — ChatGPT detected something that prevents the Skill from being used.

---

## 4. Verify that the Skill was created

After the upload succeeds:

1. Go to **Plugins → Skills**.
2. Open **Created by me**.
3. Find `lcom-business-context`.
4. Open it and confirm that the Skill is available.

At this point, do not share it with the entire workspace yet.

---

## 5. Test the Skill yourself first

Install or enable the Skill for your own account if ChatGPT asks you to do so.

Start a new chat and try several questions that should use your business knowledge, for example:

```text
What is an LCom Customer?
```

```text
Explain the relationship between a School, District, and Customer.
```

```text
What is True ARR?
```

```text
Can Usage be reported by Salesforce Product?
```

Check that the answers reflect the definitions in your `ontology/` and `knowledge/` files.

You can also explicitly select or `@`-mention the Skill when testing it.

---

## 6. Share the Skill with Reporting & Analytics

When you are satisfied with the test:

1. Go to **Plugins → Skills**.
2. Find `lcom-business-context`.
3. Select the **•••** menu next to the Skill.
4. Select **Share**.
5. Under access, search for your workspace group:

```text
Reporting & Analytics
```

6. Select that group.
7. Save the sharing settings.

Use access for the specific group rather than publishing the Skill to the whole Learning.com workspace.

---

## 7. What Reporting & Analytics users should do

After you share the Skill, a Reporting & Analytics user can:

1. Open **Plugins → Skills**.
2. Open **Shared with me**.
3. Find `lcom-business-context`.
4. Select **•••**.
5. Select **Install** if installation is required.

After installation, ChatGPT can use the Skill automatically when it determines that the Skill is relevant.

Users can also explicitly invoke the Skill by selecting or `@`-mentioning it.

---

## 8. If you cannot find Plugins or Skills

If **Plugins**, **Skills**, **Create**, or **Upload from your computer** is missing, your workspace permissions may not allow Skill creation or uploading.

Ask a Learning.com ChatGPT workspace administrator to check:

```text
Workspace settings
→ Permissions & roles
```

The relevant permissions are:

- **Enable skills**
- **Enable skill uploading**
- **Share skills**
- **Enable skills installing**

You do **not** need permission to publish Skills to the entire workspace if you only want to share the Skill with the Reporting & Analytics group.

---

## 9. If Reporting & Analytics does not appear when sharing

The workspace group must exist and be available to you in the sharing dialog.

If you cannot find the group:

1. Do not publish the Skill to everyone as a workaround.
2. Ask the ChatGPT workspace administrator whether a **Reporting & Analytics** group exists.
3. Ask them to create the group or give you permission to share with it if necessary.

You can also initially share with a few named coworkers individually if group management is not ready yet.

---

## 10. Updating the Skill later

Keep your local folder as the source that you edit:

```text
lcom-business-context/
└── skill/
    ├── SKILL.md
    ├── ontology/
    └── knowledge/
```

When you make changes:

1. Update the local Markdown files.
2. Create a new ZIP from the contents of `skill/`.
3. Update or replace the workspace Skill using the Skill management options available in ChatGPT.
4. Test the updated version before relying on it for business questions.

Git is not required for this workflow. You can introduce Git later when you want version history, peer review, rollback, or a formal release process.

---

# Minimal workflow

```text
Local Skill files
       ↓
Create ZIP
       ↓
Sign in to Learning.com ChatGPT workspace
       ↓
Plugins
       ↓
Skills
       ↓
Create
       ↓
Upload from your computer
       ↓
Test the Skill yourself
       ↓
Share
       ↓
Reporting & Analytics
       ↓
Team members install/use the Skill
```

## Recommended first rollout

For the first version, keep the audience small:

```text
You
 ↓
2–3 Reporting & Analytics users
 ↓
Validate answers and Skill triggering
 ↓
Fix knowledge or SKILL.md instructions if needed
 ↓
Expand to the full Reporting & Analytics group
```

This lets you validate both the business knowledge and how reliably ChatGPT decides when to use the Skill before exposing it more broadly.
