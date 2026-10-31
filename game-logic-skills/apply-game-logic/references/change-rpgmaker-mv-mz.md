# RPG Maker MV / MZ Gameplay Change Guidance

Load only **after** the shared change-design.md has established behavioral scope and chosen a permitted mechanism class. This guide refines implementation points for that class. Do not select or rank mechanisms during analysis.

## Implementation within the selected mechanism class

- **Editor/database:** For an authorized editable project, use the Database, Event Editor or Plugin Manager when the selected change is expressible there. Preserve IDs, referenced commands and JSON/event structure.
- **Separate plugin:** For a plugin-based change, add a distinct compatible file under `js/plugins/`, then register and enable it via Plugin Manager (reflected in `js/plugins.js`). Verify that it loads in the intended order during playtest; a file on disk or passing `node --check` is not enough. Alias only evidenced methods while preserving arguments, return value and `this`; account for subsequent overrides.
- **Event-local edit:** Target the exact event/page/command or common-event ID; preserve other pages, branches, terminators, conditions, indentation and order.
- **Reversible runtime experiment:** Observe or wrap a narrow evidenced boundary and restore the prior state. `Scene_` or `Sprite_` hooks are not automatically authoritative state writes.

## Edition-specific commands and event serialization

- MV raw plugin command: code 356, parameter containing a command string; handlers commonly override Game_Interpreter.prototype.pluginCommand.
- MZ structured plugin command: code 357, parameters = [pluginName, commandName, displayLabel, argsObject]; runtime consumes 0, 1 and 3 through PluginManager.callCommand/registered handlers. MZ projects may still have legacy 356.
- Script commands 355 followed by 655 continuation lines form one script. Preserve their execution order, context, wait/async behavior and page scoping.

## Validation

Compare the changed rule with its control state at material actors, event sources, plugin overrides, page refreshes and save/load transitions. Validate JSON/event structure and use `node --check` where available; runtime behavior still requires RPG Maker playtest/F8 DevTools/F9 debugging. Retained change provenance and rollback follow the shared application contract.
