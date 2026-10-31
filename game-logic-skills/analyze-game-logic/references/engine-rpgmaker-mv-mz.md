# RPG Maker MV / MZ Engine Adapter

Apply this specialized source/JSON/JavaScript adapter when the material gameplay path belongs to RPG Maker MV or MZ. Inherit evidence states, permission limits, depth selection, and the analyze/apply division from the parent SKILL.md. Do not treat this adapter as a request to modify the target.

## 1. Applicability and detection

Use corroborating project structure rather than JavaScript/NW.js alone:

- MV strong identification: js/rpg_core.js plus data/System.json; Game.rpgproject can corroborate a source project.
- MZ strong identification: js/rmmz_core.js plus data/System.json; Game.rmmzproject can corroborate a source project.
- Supporting data: js/plugins.js, js/plugins/, rpg_objects.js or rmmz_objects.js, data/Map###.json and data/CommonEvents.json.
- Look in the supplied root and plausible deployment subdirectories such as www/, Game/www/, assets/www/, app.nw/, resources/app/, or package.nw/.

HTML, Pixi, NW.js, package.json, and a JS filename are insufficient to prove RPG Maker identity. Data/System.json and js/plugins.js alone also do not determine edition. Both cores or conflicting project markers mean *ambiguous*, not a forced MV/MZ decision. One surviving marker may justify *probable*, but not an unqualified confirmed engine. XP, VX, VX Ace, 2000 and 2003 are outside this adapter.

**Routing precedence:** Once MV/MZ is evidenced, analyze RPG Maker data and lifecycle here first. Load the general Web/JavaScript adapter only when a distinct, material JavaScript bundle, obfuscation, worker, WASM, or other boundary needs it. Normal rpg_*.js, rmmz_*.js, and readable plugin JS are not production bundles requiring webcrack/Wakaru.

## 2. Implementation model and gameplay semantics

| Mechanic concept | Primary anchors | Caveat |
| --- | --- | --- |
| Database definitions | data/Skills.json, Items.json, Actors.json, Enemies.json, States.json, System.json | Inputs to a rule, not necessarily authoritative behavior after plugin overrides |
| Event control flow | data/Map###.json events/pages and CommonEvents.json; Game_Interpreter | Event conditions, triggers, priority, wait mode and page refresh can change timing |
| Switch/variable state | $gameSwitches, $gameVariables, $gameSelfSwitches; commands 121/122/123 | Check save lifetime, self-switch map/event scope, and other users of the same ID |
| Movement/map | Game_Map, Game_Event, Game_Player, Game_Character/Base | Transfers, move routes and scheduler ownership matter |
| Battles | Game_Action, Game_Battler, BattleManager plus skill/state databases | Resolve formula order, crit/variance/rounding/RNG and overridden methods from evidence |
| Inventory/economy | Game_Party, item/weapon/armor databases, shop event commands | Plugins may override inventory or pricing |
| Persistence | DataManager, StorageManager and $game* state | Save contents and load/reset timing depend on runtime and plugins |
| Rendering | Scene_*, Window_*, Sprite_*, Pixi | Visual consumers do not prove authoritative state mutation |

MV conventionally uses engine scripts named rpg_*.js, whereas MZ uses rmmz_*.js. Custom builds may diverge: validate the installed version and material files.

## 3. Engine-specific semantic anchors

1. Parse the generated js/plugins.js manifest safely as its JSON-literal array assignment; preserve enabled status, load order, name and parameters. Never eval project JavaScript for an inventory.
2. Locate text, state IDs, skills, enemies, item IDs, event IDs and common-event calls in the database. Follow the relevant event pages, commands and plugin handlers before reading the entire engine.
3. Useful event command codes include 111 (conditional branch), 117 (common event), 121 (switches), 122 (variables), 123 (self switch), 355 plus following 655 lines (script), 356 (legacy raw plugin command) and 357 (MZ structured plugin command). This is a lookup subset, not a complete event schema.
4. MV usually reaches plugin commands through Game_Interpreter.prototype.pluginCommand(command, args); a 356 event stores a raw command string. Plugin-specific parsing controls its semantics.
5. MZ uses PluginManager.registerCommand(pluginName, commandName, callback). For a normal 357 event, parameters[0] is the plugin name, [1] command name, [2] editor display label, and **[3] is the arguments object**. MZ may also support 356 via legacy compatibility or plugin hooks: inspect the actual handler.
6. Plugin metadata such as @param, @type, @default, @command and @arg describes editor parameters, not proof of runtime handlers or numeric types. Values returned by PluginManager.parameters may require explicit conversion.

## 4. Runtime values, ownership and lifecycle

Distinguish $data* database records from mutable $game* instances. Preserve 1-based database IDs and array holes. Trace local event/page state, self switches, actor/enemy instances, party-wide state, map state, and shared definitions separately. Resolve the **effective** implementation with the actual ordered enabled plugin set; a vanilla engine function is not necessarily the function executing at runtime. Inspect wait modes, interpreter nesting, parallel/autorun scheduling, page refresh and save/load only when material to the question.

## 5. Recommended tracing workflow

1. Identify project root and MV/MZ edition using multiple markers; record version evidence and hashes for relevant core, plugin manifest, data and plugins.
2. Inventory relevant database IDs and map/common/troop events; locate event/page/command indexes and conditions.
3. Trace from event or database anchor through Game_Interpreter, embedded script, plugin command and callbacks.
4. Read js/plugins.js in actual order and locate aliases, prototype overrides and command registrations; identify which definition and mutation can execute.
5. Separate authoritative writes from read-only presentation, state serialization and save/load.
6. Use playtest and F8 DevTools/F9 debug views when runtime evidence is required; compare with control state and restore experiments.
7. Report compact version-scoped pseudocode, locators (file, database ID, event/page/command or plugin function/line), material uncertainty and validation state.

## 6. Static analysis

Use JSON-aware parsing for event arrays and IDs. Keep event command ordering, indentation, page conditions, triggers, and 355/655 continuations intact. Start JavaScript searches with text/rg. Use a JavaScript AST parser such as Babel or tree-sitter for precise definitions, alias/override graph reconstruction, and dynamic registrations if regex hits are inadequate. Regex matches are **candidates**, not proof of runtime execution or last-writer ownership. Do not run web bundle decomposition on ordinary readable engine/plugins.

## 7. Runtime observation

Prefer the game's matching RPG Maker editor playtest, F8 developer tools and F9 variable/switch debug screen. Observe narrow Game_Interpreter, Game_Action, DataManager, or plugin callback boundaries only where needed. Use pure function fixtures for truly independent logic. A Node syntax check is not gameplay validation; browser automation is not equivalent to NW.js behavior if NW-specific dependencies matter.

## 8. Version-sensitive assumptions

Retain MV/MZ edition, actual core hashes, material plugin names/order/hashes and database hashes. Core scripts may be customized. Revalidate command registration, event data shapes, script execution order, animation/saving differences, and plugin modifications against the target build. Do not replace local facts with assumptions from an upstream core-script repository.

## 9. Common failures

- Routing by generic NW.js/Pixi signals or unpacking ordinary readable RPG Maker sources.
- Inferring effective state ownership from vanilla engine functions, regex hits or presentation hooks without tracing enabled plugins.
- Losing event/page/script continuation context or reading MZ command 357 arguments from index 2 rather than 3.

## 10. Evidence checklist

Keep edition/build evidence, relevant database and event/page/command locators, effective enabled-plugin order, authoritative state mutations, and any material save/wait uncertainty; distinguish observed from inferred behavior.
