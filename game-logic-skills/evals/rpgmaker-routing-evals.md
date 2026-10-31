# RPG Maker MV/MZ routing and composition evaluations

Treat scenarios as PASS/FAIL. Classification must not run project JavaScript, and no test may write to installed game data.

## 1. MZ identity overrides generic NW.js detection

Given www/index.html, package.json, Pixi assets, js/rmmz_core.js, js/plugins.js and data/System.json, a request about a common-event variable must dispatch to the RPG Maker analysis adapter. It must inspect data/CommonEvents.json and relevant switch/variable paths instead of starting Web/JS bundle recovery.

## 2. MV raw plugin command and effective override

Given js/rpg_core.js, data/System.json, an event with command 356, and plugin A enabled before plugin B, trace actual handler and aliases in load order; ignore disabled plugins. Preserve raw command text and do not treat the base rpg_objects.js definition as necessarily effective.

## 3. MZ command 357 argument payload

A map event records code 357 with parameters ["Foo","set","Set title",{"title":"Act 2"}]. Verify registered Foo:set command and the arguments **at index 3**; index 2 is editor-facing display text.

## 4. Web JS false positive

Given only HTML, package.json, Pixi and a custom bundled JS entry, without RPG Maker core files, project markers or corroborated database, do not select RPG Maker. Generic Web/JS remains viable.

## 5. Mixed markers and opaque deployment

Both MV and MZ core files or contradictory edition markers produce ambiguous classification. A mere NW.js bootstrap with inaccessible container does not infer a specific edition; stay read-only until identifying evidence is available.

## 6. Analysis/application separation

When the user wants an authorized local one-actor adjustment, analyze returns exact mechanic, ownership/fan-out and version facts without choosing a write mechanism; apply then selects a viable class, uses RPG Maker change guidance (not generic Web/JS for ordinary plugins), tests against other actors and save/load, and avoids installed-file edits by default. For a new plugin, apply confirms Plugin Manager registration, enabled status and runtime loading before claiming success.
