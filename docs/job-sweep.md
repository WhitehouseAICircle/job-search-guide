# Job Sweep: a regular search for potential roles

[Back to the guide](../README.md) · [More prompts](example-chats.md)

A chat called **Job Sweep** can help you look for publicly advertised roles that fit your preferences. Where scheduled tasks are available, you can ask it to repeat the search each morning and return a short list to review. You choose which roles to pursue and send applications yourself.

**This is an optional example, not a live job-search service.** The prompts below have not been tested as an unattended scheduled search. No recurring task has been activated for this demo, and the existing screenshots show the earlier fictional application exercises.

## 1. Choose your filters

Start a chat inside your job-search Project and call it **Job Sweep**. The name is just for organisation. Give it clear preferences; you do not need to upload a CV or share your full home address.

| Filter | Example to adapt |
| --- | --- |
| Role types | Entry-level administrator or customer service assistant |
| Area | Within 10 miles of [town or city] |
| Workplace | On-site or hybrid; fully remote roles also considered |
| Hours | 18–25 hours a week; specify days you can work if useful |
| Salary | £24,000–£28,000 a year full-time equivalent, with part-time pay clearly identified |
| Contract | Permanent preferred; consider fixed-term roles of at least six months |
| Exclusions | Commission-only, unpaid roles and any vacancy asking applicants to pay a fee |
| Sources | Employer careers pages and publicly accessible job listings; add preferred sites if you have them |

These are illustrative preferences, not a claim about local vacancies or typical pay. **Full-time equivalent** means the salary for a full-time version of the role; actual part-time annual pay is usually lower. State whether your own target is actual annual pay, full-time equivalent or hourly pay. If an advert does not make this clear, ask for it to be flagged rather than guessed.

## 2. Try a search before scheduling it

Replace the bracketed location and adjust the filters before sending this prompt. Test it as an ordinary search first so you can see whether this chat has the tools and source access it needs.

```text
Help me run a Job Sweep using publicly accessible online vacancies.

My preferences:
- Roles: entry-level administrator or customer service assistant.
- Location: within 10 miles of [town or city]. Use the town only,
  not my home address. Also consider fully remote UK roles.
- Workplace: on-site, hybrid or fully remote; label which applies.
- Hours: 18–25 hours a week.
- Salary: £24,000–£28,000 annual full-time equivalent.
  State actual part-time pay separately when advertised.
- Contract: permanent preferred; fixed-term of at least six months
  may be worth considering.
- Exclude commission-only or unpaid roles and applicant fees.

For the first sweep, look for adverts dated within the last seven days.
If the posting date is missing, label it unknown; do not invent one.
Use employer careers pages where possible and include the source link.
Do not bypass logins, paywalls or other access restrictions.

Return at most five potential matches. For each, show:
role and employer; source link; location and workplace arrangement;
hours and working pattern; advertised pay and its basis;
advert date and closing date if stated; date checked;
why it may fit; and any missing detail or mismatch.
Keep roles with unconfirmed hours or salary in a separate
'Needs checking' section. Do not claim I am eligible or qualified
without evidence, and do not invent vacancies or details.

Say which sources you checked and which you could not access.
If nothing suitable is found, say 'No new matches found in the
sources checked', with any limitations. Never imply no jobs exist.
This search is for review only. Do not contact employers, submit
applications, send a CV or share my personal information.
```

Open the original links yourself. Check that each employer and vacancy is genuine, the application is still open and the hours and pay suit you. Refine the filters if the list is too broad or too narrow. A salary or working pattern marked unknown is a question to resolve, not a confirmed match.

If ChatGPT cannot search the web in this chat, use ordinary job alerts or search the sites yourself, then paste an advert into [Understanding a job advert](example-chats.md). Scheduling cannot make an inaccessible source available.

## 3. Ask for a daily schedule

Once the trial search is useful, continue in the same chat. Include the complete, final filters and search instructions in the task's saved prompt so the schedule does not depend on remembering an earlier message.

```text
Set up a scheduled task called Job Sweep using the full search
instructions and filters we have just agreed. Include those in the
saved task prompt and show them to me so I can check them.

Run every day at 08:00 in the Europe/London time zone, including
weekends. Keep the local time at 08:00 when the clocks change.

After the first run, look for additions since the last successful
sweep. Use previous results available in this chat to avoid repeating
the same vacancy, comparing job ID or URL, employer, title and location.
Distinguish 'newly found by this search' from 'newly advertised'.
If previous results or the last successful run are unavailable,
say so; do not claim the results are definitely new.

Return a short summary even if no new matches are found. Tell me
about source-access problems or incomplete searches separately.
Keep applications and employer contact for me to handle myself.

Confirm the saved schedule, time zone and next run time.
```

Check the task actually appears in **Scheduled**, with the intended prompt, time zone and next run. A chat name or a written acknowledgement alone does not prove a recurring task was saved. Availability and menus depend on your account and workspace. If scheduling is unavailable inside your Project, try a separate chat with the complete filters and instructions; otherwise keep using the manual prompt.

Once daily is a useful starting point. To change it, ask to **update the existing Job Sweep task**, for example to weekdays at 08:00, or to 08:00, 13:00 and 18:00 Europe/London each day, if supported. Check the saved schedule afterwards and avoid creating duplicate tasks. More frequent searches do not guarantee more vacancies.

Web-based tasks depend on the tools and sources available to that chat. A task using files in a local desktop project has different requirements: the computer and app need to be running. Do not build this simple sweep around private files on your computer.

## 4. Check notifications on your devices

A completed run should leave results for you to read in the task or continuing chat. To receive an alert, check **Settings → Notifications** and the task settings available on your account. Delivery channels vary; enable the supported completion alerts you want and allow the relevant browser, app or operating-system permissions.

Use the same ChatGPT account on your phone and computer. Where mobile push or desktop notifications are supported and enabled, these can let you know a sweep has finished. **An alert on both devices is not guaranteed.** Check a first completed run and its notification before relying on the routine. If no alert arrives, open **Scheduled** and the chat to check whether the task ran, then review permissions and settings.

Treat an alert as a reminder to read the result, not proof that a suitable job was found. The summary may say there were no new matches, or that some sources could not be checked.

## 5. Review the shortlist and choose a next step

An illustrative summary might look like this:

> **Example only — no live vacancies:** One potential role to review and one advert needing an hours or salary check. Open each original advert, confirm the details, then choose whether to explore it further.

For an actual result, copy the relevant advert into **Understanding the advert**, alongside a short checked summary of your experience. Then use the existing CV, supporting statement and interview prompts. Keep your own application record; a shortlist entry is not an application.

Search coverage and duplicate detection are imperfect. Keep any useful employer or job-board alerts too. ChatGPT cannot find an unpublished vacancy or reliably inspect a listing behind an inaccessible login. For a role shared offline, supply a short anonymised description or the advert text yourself; make clear that it needs checking rather than claiming it was verified online.

## Keep the sweep private and manageable

- Use a town or search area rather than your home address or full postcode.
- Keep CVs, phone numbers, identity documents and private recruiter messages out of the sweep.
- Review the provider's data controls before supplying sensitive information; cloud services may process or store what you share.
- Pause or remove the task in Scheduled when you no longer need it, and review saved filters when your preferences change.

See the [privacy notes](privacy-notes.md) before sharing any screenshots or results with the Circle.

## Sources and status

Feature guidance checked on **7 November 2026** against OpenAI's [Scheduled tasks guide](https://learn.chatgpt.com/docs/automations) and [Notifications guide](https://learn.chatgpt.com/docs/notifications). These describe scheduling, source access and notification controls; they do not guarantee comprehensive job coverage or notification delivery on every device. Menus and availability may change.

The filters, prompts and sample summary here are educational examples. An unattended job sweep and its notifications have not been tested as part of this demo.
