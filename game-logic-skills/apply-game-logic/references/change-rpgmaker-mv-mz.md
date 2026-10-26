# RPG Maker MV / MZ Gameplay Change Guidance

Load only **after** the shared change-design.md has established behavioral scope and chosen a permitted mechanism class. This guide refines implementation points for that class. Do not select or rank mechanisms during analysis.

## Options within the selected mechanism class

- **Editor/database configuration:** For an editable authorized project, prefer the RPG Maker Database, Event Editor or Plugin Manager when the target rule is expressible there. Preserve IDs and dependent references; validate changed JSON schema and event structure.
- **Separate compatible plugin:** For a suitable script-level change, prefer a distinct js/plugins/UniqueName.js. Alias only evidenced method(s), preserving the original call's arguments, return value and this binding. Put it at a justified place in the *enabled* plugin order, and verify aliases and later overwrites; “put it last” is not proof of correct scope.
- **Event-local changes:** Target the exact map/event/page/command index or common-event ID. Preserve other pages, branch blocks, terminators, trigger/condition fields, indentation and command order.
- **Runtime experiment:** Use a narrow reversible wrapper or observation boundary during test play. Keep restoration data. A Scene_ or Sprite_ hook is not automatically an authoritative battle or inventory change.
- **Destructive installed-file change:** Require explicit authorization and integrity-verifiable originals and rollback as in the shared core. Use a copy otherwise.

## Edition-specific commands and event serialization

- MV raw plugin command: code 356, parameter containing a command string; handlers commonly override Game_Interpreter.prototype.pluginCommand.
- MZ structured plugin command: code 357, parameters = [pluginName, commandName, displayLabel, argsObject]; runtime consumes 0, 1 and 3 through PluginManager.callCommand/registered handlers. MZ projects may still have legacy 356.
- Script commands 355 followed by 655 continuation lines form one script. Preserve their execution order, context, wait/async behavior and page scoping.

## Validation and delivery

Compare unchanged and changed behavior on the same state, including materially shared actors, event sources, competing plugins, page refresh, save/load and scene transitions. Verify the effective enabled plugin order and exact targeted version/build/hash. Keep the recovered mechanic, changed files, original content/hash, tests and rollback procedure together using application-artifacts.md.

Use Python JSON parsing/schema checks for data edits, node --check for JS syntax where available, and RPG Maker playtest/F8 DevTools/F9 debugging for engine behavior. Passing a syntax check alone does not establish runtime correctness.
