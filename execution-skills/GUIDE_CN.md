## Assistant

我扫描了当前项目，发现共有 10 个 Skill，版本均为 `v5-rc.1`。它们共同组成一套面向长期维护型软件项目的工程协作体系。

最重要的总原则是：

> “是否相关”不等于“是否可以调用”。
> 部分 Skill 可以根据任务类型调用，部分 Skill 必须由用户或上游编排器显式选择。

## 一、总体分类

| 类型 | Skill | 主要职责 |
|---|---|---|
| 模型调用型 | `engineering-implementation` | 实现、修复、重构代码 |
| 模型调用型 | `engineering-investigation` | 调查、诊断、测量、复现、研究 |
| 模型调用型 | `engineering-review` | 审查、验收、判断是否符合要求 |
| 模型调用型 | `engineering-specification` | 编写需求、规格说明或 RFC |
| 模型调用型 | `engineering-execution-planning` | 制定具体执行计划 |
| 模型调用型 | `engineering-knowledge-governance` | 管理规范、设计、文档和知识的生命周期 |
| 模型调用型 | `engineering-handoff` | 跨 Agent、会话或执行者交接工作 |
| 显式编排型 | `engineering-foundation-design` | 建立或重置项目基础架构 |
| 显式编排型 | `engineering-plan-and-delegate` | 规划、拆解并委派实际工作 |
| 显式编排型 | `engineering-initiative-shaping` | 将 Large 级别 initiative 拆解为多个 Medium 需求 |

显式编排型 Skill 不能仅因为任务复杂、文件多或风险高就自动启用。

---

## 1. `engineering-implementation`

源文件：[engineering-implementation/SKILL.md](E:/Home/projects/skills/engineering-implementation/SKILL.md)

### 用途

用于已经获得授权的持久化代码修改，包括：

- 实现新功能；
- 修复 Bug；
- 重构代码；
- 修改测试、配置或相关工程文件；
- 根据已接受的设计进行实际落地。

它的核心工作模式是：

> Intent → Feedback → Evidence
> 意图 → 反馈 → 证据

也就是说，先明确要达到什么结果，再通过测试、实验和代码检查不断反馈，最后用证据证明修改确实正确。

### 适用场景

例如：

- “给 API 增加分页功能。”
- “修复登录超时问题。”
- “把这个模块重构成依赖注入方式。”
- “根据已批准的 RFC 实现数据迁移。”
- “修改序列化格式，并同步更新相关测试。”

### 重要边界

它只负责被授权的工作树修改，并不会自动获得以下权限：

- `git commit`、`git push`；
- 切换分支；
- 发布、部署；
- 修改远程系统；
- 更新凭据；
- 删除重要数据。

如果请求是“调查问题，如果确认是原因 X 就修复”，首先应使用调查或审查能力。只有确认条件成立并且确实开始修复时，才进入 implementation。

### 验证要求

不能只证明“新功能能运行”，还要检查：

- 是否引入回归；
- 是否破坏已有契约；
- 是否违反模块边界；
- 是否扩大了不必要的范围；
- 是否增加了无必要的复杂度；
- 基线失败和新引入失败是否被区分。

---

## 2. `engineering-investigation`

源文件：[engineering-investigation/SKILL.md](E:/Home/projects/skills/engineering-investigation/SKILL.md)

### 用途

用于获取事实和证据，而不是直接修改生产代码。核心循环是：

> Question → Probe → Evidence → Implication
> 问题 → 探针 → 证据 → 结论影响

### 适用场景

例如：

- 调查某个 Bug 的根因；
- 复现线上错误；
- 测量性能回归；
- 研究某个 API、库或协议的行为；
- 比较多个技术方案；
- 判断某个假设是否成立；
- 编写一次性的实验或原型；
- 进行只读技术审计。

### 典型做法

应先提出一个尽可能小的问题或假设，然后设计能区分不同解释的探针，例如：

- 最小复现；
- 针对性测试；
- 控制输入变化；
- 性能基准；
- 临时日志或 instrumentation；
- 一次性 prototype；
- 阅读官方规范或源码。

### 重要边界

默认不应：

- 修改受版本控制的生产代码；
- 更新依赖或 lockfile；
- 接受快照；
- 把临时实验留下作为正式实现；
- 因为发现问题就自动修复。

如果调查结果确认了需要修复的问题，并且用户授权继续修改，才转入 `engineering-implementation`。

### 输出内容

调查结果通常应包括：

- 回答了什么问题；
- 最强证据是什么；
- 结论及可信度；
- 支持和反驳该结论的证据；
- 环境限制；
- 是否需要后续设计决策或代码修改。

---

## 3. `engineering-review`

源文件：[engineering-review/SKILL.md](E:/Home/projects/skills/engineering-review/SKILL.md)

### 用途

用于只读地判断某个已有工程成果是否应该被接受，包括：

- 代码实现；
- Diff；
- Pull Request；
- 设计；
- 规格说明；
- 配置或其他工程产物。

它不是简单的“测试是否通过”，而是要求同时检查正面和负面证据。

### 两个审查维度

#### 正面证据

确认目标是否真正实现：

- 需求是否满足；
- 边界和错误行为是否符合约定；
- 兼容性和迁移行为是否正确；
- 测试是否真正覆盖目标行为；
- 系统的可观察结果是否正确。

#### 负面证据

确认不应该出现的状态没有出现：

- 是否破坏架构边界；
- 是否破坏公共契约；
- 是否引入回归；
- 是否扩大了无关范围；
- 是否增加了不必要的耦合、抽象或依赖；
- 是否产生重复的事实来源；
- 是否增加了没有理由的维护负担。

### 适用场景

例如：

- “审查这个 PR 是否可以合并。”
- “验证这个实现是否符合 RFC。”
- “检查重构是否破坏了模块边界。”
- “评估这个设计是否可接受。”
- “判断迁移是否完成。”

### 输出结果

通常会分别给出：

- 需求意图：PASS / FAIL / INCOMPLETE；
- 约束和设计：PASS / FAIL / INCOMPLETE；
- 回归和非预期影响：PASS / FAIL / INCOMPLETE；
- 复杂度和维护负担；
- 总体结论：ACCEPT / REJECT / INSUFFICIENT EVIDENCE。

审查本身是只读的。发现问题并不自动授权修复。

---

## 4. `engineering-specification`

源文件：[engineering-specification/SKILL.md](E:/Home/projects/skills/engineering-specification/SKILL.md)

### 用途

用于明确“要做什么、为什么做、必须满足什么约束，以及采用什么工程方向”。

它关注的是：

> What / Why / Constraints / Accepted Approach

### 适用场景

只有在以下情况适用：

- 用户明确要求写需求、规格说明或 RFC；
- 用户要求确定工程设计；
- 上游编排流程要求在执行前先形成规格；
- 需要把讨论结果整理成可审查、可执行的设计契约。

例如：

- “写一个 API 版本升级规范。”
- “设计新的缓存架构。”
- “把这个需求整理成 RFC。”
- “明确数据迁移的兼容策略和验收标准。”

### 规格通常应涵盖

- 问题和目标结果；
- 范围与非目标；
- 当前系统状态；
- 可观察的需求和验收行为；
- 必须保持的约束与不变量；
- 已接受的工程方向；
- 受影响的模块、接口、数据模型和集成边界；
- Fixed / Local / Open 决策；
- 验证意图；
- 尚未解决的问题。

### 重要区别

规格说明不是执行计划：

- 规格说明回答“要实现什么、为什么、采用什么方向”；
- 执行计划回答“按什么顺序、由谁、以哪些工作单元和验证点完成”。

如果用户只要求 RFC 草案，可以保留 Open 问题，不必强行把它变成可立即实现的设计。只有用户要求“implementation-ready specification”时，阻塞性决策才必须解决。

---

## 5. `engineering-execution-planning`

源文件：[engineering-execution-planning/SKILL.md](E:/Home/projects/skills/engineering-execution-planning/SKILL.md)

### 用途

将已经接受的需求和设计转换成可以执行的协调计划。

它关注的是：

> Sequence / Dependencies / Work Units / Verification / Handoffs

### 适用场景

例如：

- “请把这个 RFC 拆成具体实施步骤。”
- “制定数据库迁移的执行计划。”
- “规划这个功能的开发顺序和验证方式。”
- “明确哪些工作可以并行，哪些必须串行。”

### 好的计划应明确

- 每个工作单元的可观察结果；
- 真实的依赖关系；
- 哪些任务可以独立验证；
- 共享可变区域；
- 每个工作单元的 Fixed / Local / Open 决策；
- 正面和负面验证方式；
- 实际交接点；
- 什么证据会触发重新规划。

通常更偏好垂直切片，例如“从接口到存储完成一条可验证路径”，而不是机械地拆成“先改所有模型、再改所有服务、最后改所有测试”。

### 重要边界

如果仍存在重大产品、架构、兼容性、安全或数据决策，不应偷偷把这些决策塞进实施任务，而应返回规格或设计阶段。

它本身也不等于 delegation。计划可以说明“哪些工作将来适合委派”，但只有真的跨执行者时才需要 `engineering-handoff`。

---

## 6. `engineering-knowledge-governance`

源文件：[engineering-knowledge-governance/SKILL.md](E:/Home/projects/skills/engineering-knowledge-governance/SKILL.md)

参考：[knowledge-model.md](E:/Home/projects/skills/engineering-knowledge-governance/references/knowledge-model.md)

### 用途

管理工程知识是否需要持久化、应该放在哪里、谁是权威来源，以及如何处理过时、重复或相互矛盾的文档。

它管理的是：

- 规格；
- 架构设计；
- ADR；
- 契约；
- Runbook；
- 工程约定；
- 重要调查结论；
- 必须跨上下文保存的计划或交接状态。

### 适用场景

只有当出现具体知识治理问题时才使用，例如：

- 新实现使现有 API 文档过时；
- 一个旧设计已经被新设计取代；
- 多份文档描述了互相矛盾的当前状态；
- 调查结果会影响未来多个任务；
- 需要移动、合并、拆分或退休某个规范；
- 跨 Agent 工作需要保存最小的连续性状态。

### 核心原则

它不主张“每次写代码都写文档”。持久化前需要判断：

- 没有这条知识，未来执行者是否可能做出明显更差的决定；
- 以后重新推导它是否昂贵、含糊或有风险；
- 是否会导致已有权威来源不完整或误导；
- 是否确实需要跨会话或跨 Agent 连续性。

优先更新已有的权威来源，不要额外创建平行的“第二真相”。

### 重要边界

这个 Skill 不自动获得文档修改权限。如果底层任务是只读的，就只能报告需要治理的地方，不能擅自编辑仓库文档。

---

## 7. `engineering-handoff`

源文件：[engineering-handoff/SKILL.md](E:/Home/projects/skills/engineering-handoff/SKILL.md)

### 用途

在实际发生 Agent、模型、会话、上下文或执行者切换时，创建一个足够完整但不过度冗长的交接契约。

### 适用场景

例如：

- 一个 Agent 完成调查，另一个 Agent 接着实现；
- 上下文即将结束，需要保存恢复状态；
- 一个开发者完成计划，另一个开发者负责执行；
- 工作拆分后，子任务交给独立执行者；
- 实施中途需要暂停，之后恢复。

### 交接内容

交接至少应包含：

- 目标结果；
- 范围和非目标；
- 权威规格、设计和契约；
- Fixed 决策；
- 接收者可以自行决定的 Local 事项；
- 必须上报的 Open 决策；
- 真实依赖和顺序；
- 正面和负面验证方式；
- 触发重新规划或升级的条件；
- 已完成工作、部分完成工作、剩余工作；
- 已执行的检查及其结果；
- 尚未验证的部分；
- 下一步可直接执行的动作。

特别强调：必须区分“计划执行的检查”和“已经实际执行且观察到结果的检查”。

### 重要边界

仅仅因为任务复杂、已经制定计划，或者任务被标记为 Medium/Large，并不代表发生了 handoff。只有实际跨越执行边界时才需要它。

交接文档默认是临时协调状态，除非确实需要跨上下文持续保存。

---

## 8. `engineering-foundation-design`

源文件：[engineering-foundation-design/SKILL.md](E:/Home/projects/skills/engineering-foundation-design/SKILL.md)

### 用途

用于建立或实质性重置项目、系统或子系统的基础工程架构，包括：

- 架构边界；
- 模块职责；
- 依赖方向；
- 核心接口和契约；
- 数据模型；
- 关键不变量；
- 工程约定；
- 验证策略。

### 适用场景

这是显式编排型 Skill，必须由用户或有授权的上游流程选择。适用于：

- 新项目建立基础架构；
- 新子系统正式确定模块边界；
- 重置已有基础架构；
- 重新定义关键公共契约；
- 基础部署、持久化、安全或并发模型发生重大改变。

### 使用前提

它要求先确认：

- 使用的模型和推理能力足以处理重要架构决策；
- 必要时可以访问网络或外部技术资料；
- 项目中没有被忽略的已有基础约束；
- 如果要重置已有基础，用户确实理解并接受其影响。

因此，不能把一个未检查的仓库当成“空白项目”。

### 输出内容

目标是形成一份尽可能薄但足够可靠的基础工程契约，包括：

- 系统目标和非目标；
- 组件及边界；
- 依赖方向；
- 核心约束和不变量；
- 外部与内部契约；
- 必要的工程约定；
- 验证策略；
- 未决的重大问题；
- 权威信息的存放位置。

### 与 Large initiative 的区别

- `foundation-design` 关注“基础架构是否要建立或重置”；
- `initiative-shaping` 关注“一个大型目标如何拆分成多个阶段”。

Large 不等于 bootstrap。一个小型子系统可能需要 foundation design，而一个大型迁移项目也可能完全不需要重置基础架构。

---

## 9. `engineering-plan-and-delegate`

源文件：[engineering-plan-and-delegate/SKILL.md](E:/Home/projects/skills/engineering-plan-and-delegate/SKILL.md)

### 用途

这是显式的规划、拆解和委派编排模式。它的职责不是亲自完成所有计划细节，而是决定：

1. 当前意图是否已经足够明确，可以开始规划；
2. 应该采用什么拆解和协调策略；
3. 哪些地方发生了真实的执行交接。

它通常会组合：

- `engineering-execution-planning`；
- `engineering-handoff`；
- `engineering-knowledge-governance`。

### 适用场景

例如：

- 用户明确要求“拆成多个子任务并委派”；
- 用户要求设计多 Agent 协作流程；
- 需要判断是一个执行者直接完成，还是拆分给多个执行者；
- 需要协调多个有明确边界的工作包。

### 关键特点

它并不强制拆分任务。如果一个执行者可以安全完成并验证，也可以选择直接执行。

拆解时重点不是最大化并行，而是：

- 工作单元是否可独立验证；
- 是否存在真实依赖；
- 是否减少共享可变范围；
- 接收者是否能在不重新设计系统的情况下执行；
- 是否保留 Fixed 决策并暴露 Open 决策。

执行者能力应根据“剩余决策负担和后果”选择，而不是根据文件数量或工作量标签选择。

---

## 10. `engineering-initiative-shaping`

源文件：[engineering-initiative-shaping/SKILL.md](E:/Home/projects/skills/engineering-initiative-shaping/SKILL.md)

### 用途

用于显式选定的 Large initiative，将一个跨阶段的大目标塑造成：

1. 清晰的宏观目标；
2. 稳定的跨阶段设计；
3. 多个可以独立进入 Medium 工作流的需求单元。

它不负责在一个上下文中解决整个大型项目。

### 适用场景

例如：

- 大规模系统迁移；
- 平台重构；
- 多阶段数据迁移；
- 多团队协作的基础设施升级；
- 需要先研究、再设计、再逐步切换的长期 initiative。

### 工作内容

它会先确定：

- 最终目标和原因；
- 非目标；
- 跨阶段不变量；
- 兼容性与迁移边界；
- 安全、数据、运维和组织约束；
- 成功标准。

然后讨论可能的路线：

- 目标架构；
- 迁移形状；
- 兼容策略；
- 并行或串行顺序；
- 灰度、共存和切换方案；
- 需要先验证的未知因素。

最终需要区分：

- 已接受的宏观决策；
- 被拒绝但值得记录的方案；
- 仍需研究或决策的 Open 问题。

### 拆分结果

拆分出来的单元不一定全是编码任务，也可能是：

- 实现需求；
- 迁移需求；
- 调查或 prototype 需求；
- 兼容性决策需求；
- 运营切换需求；
- 验证和上线需求。

每个单元都应该有明确结果、依赖关系、治理约束和验收意图。

### 重要边界

不能仅凭“文件很多”“架构很复杂”“风险很高”就推断这是 Large。Large 是用户或上游流程定义的容量和协作边界。

它完成后应停止在宏观层面，后续每个 Medium 单元再分别进入规格、计划、实施、审查和验收流程。

---

## 二、几个容易混淆的 Skill

### Investigation、Review、Implementation 的区别

| 问题 | 应使用 |
|---|---|
| “系统现在到底发生了什么？” | `engineering-investigation` |
| “这个实现是否符合要求、是否可以接受？” | `engineering-review` |
| “请把它改好并提交代码修改。” | `engineering-implementation` |

典型流程可能是：

`Investigation → Review/Decision → Implementation → Review`

但不是每个任务都必须经过完整链条。

### Specification、Execution Planning、Handoff 的区别

| Skill | 解决的问题 |
|---|---|
| Specification | 做什么、为什么做、哪些约束必须满足 |
| Execution Planning | 按什么顺序、分成哪些工作、如何验证 |
| Handoff | 交给另一个执行者时，如何保证其不会误解或重新设计 |

### Foundation Design、Initiative Shaping、Plan and Delegate 的区别

| Skill | 核心问题 |
|---|---|
| Foundation Design | 基础架构和核心契约应该是什么 |
| Initiative Shaping | 大型目标如何形成宏观路线并拆成阶段 |
| Plan and Delegate | 已接受的工作如何规划、拆分和委派 |

---

## 三、项目中反复出现的共同概念

### Fixed / Local / Open

所有非平凡任务都应尽量区分：

- **Fixed**：已经确定的产品行为、架构、契约、兼容性和范围，不能随意改变；
- **Local**：可逆的实现细节，执行者可以自主选择；
- **Open**：尚未解决且有实质影响的决策，不能悄悄在代码里决定，必须升级或明确委派。

### 正面证据与负面证据

项目不接受“测试通过”作为唯一证明。

- 正面证据：目标功能确实实现；
- 负面证据：没有引入回归、架构违规、契约破坏、范围蔓延或不必要复杂度。

### Small / Medium / Large 不是复杂度评分

当前项目明确规定：

- Small / Medium / Large 是用户的容量和协作策略；
- 不能通过文件数量、代码量、风险或架构复杂度自动推断；
- Skill 必须保留上游提供的工作量标签；
- 容量不足时应报告证据和建议，而不是自行改变等级或降低验收标准。

---

## 四、典型组合方式

### 小型直接修改

`用户意图 → engineering-implementation → 验证 → 必要时 engineering-review`

### 中型工程任务

`engineering-specification → engineering-execution-planning → engineering-implementation → engineering-review`

如果中间真的跨 Agent 或会话，再加入：

`engineering-handoff`

### 大型 initiative

`engineering-initiative-shaping → 多个 Medium 需求 → 每个需求分别规格化、规划、实施和验收`

### 诊断型任务

`engineering-investigation → 得出结论`

如果调查结果要求修改：

`engineering-investigation → engineering-implementation`

如果调查结果改变了系统的长期设计或文档真相，再加入：

`engineering-knowledge-governance`

### 基础架构建立

`engineering-foundation-design → specification/planning → implementation → review`

其中 `foundation-design` 必须由用户或有授权的上游编排器显式启用。

总体上，这个项目不是一套强制性的“文档流水线”，而是一组按任务边界组合的工程能力：先明确意图，再根据需要调查、设计、计划、实现、审查、交接和维护长期知识。

## User

所以从零开始一个大型项目, 且初始需求一句话就能描述, 该怎么做?

## Assistant

应该采用“两层流程”：

1. 先做一次显式的 Large initiative shaping，明确目标、路线和阶段；
2. 同时进行一次显式的 foundation design，建立不会被后续任务随意推翻的基础架构；
3. 再把大型项目拆成多个 Medium 需求，每个需求独立完成规格、计划、实现和验收。

在本项目中，推荐流程如下：

```text
一句话目标
  ↓
engineering-initiative-shaping
  ↓
engineering-foundation-design
  ↓
拆成多个 Medium 需求
  ↓
每个 Medium：
  specification
  → execution-planning
  → implementation
  → review / acceptance
  → 必要时 knowledge-governance
```

如果实际跨 Agent、模型、会话或执行者，还在交接处加入 `engineering-handoff`。如果需要多人或多 Agent 协调，再显式使用 `engineering-plan-and-delegate`。

## 1. 不要直接把一句话变成代码

一句话需求只能作为“目标方向”，通常还不足以决定：

- 谁是目标用户；
- 什么行为算成功；
- 哪些能力属于第一阶段；
- 哪些行为明确不支持；
- 数据、兼容性、安全和运维约束是什么；
- 哪些技术选择是必须固定的；
- 哪些问题还需要调查。

首先应把它扩展成一个宏观目标：

- 目标结果：系统最终要让什么事情变得真实可行；
- 用户和使用场景；
- 非目标：第一阶段明确不解决什么；
- 成功标准；
- 关键约束和不变量；
- 已知事实；
- 未知问题；
- 需要用户决策的重大选择。

要区分：

- **Fixed**：已经确定的产品、架构、兼容性和范围决策；
- **Local**：执行者可以自行选择的可逆实现细节；
- **Open**：不能偷偷在代码中决定的重大未决问题。

## 2. 先确定宏观方向

使用 `engineering-initiative-shaping`，但不是马上编写详细任务清单，而是确定：

- 项目的最终目的；
- 主要阶段；
- 跨阶段必须保持的契约；
- 兼容和迁移策略；
- 哪些风险必须提前验证；
- 哪些技术路线被接受、拒绝或暂时保留。

大型项目中经常需要先做调查，例如：

- 某个数据库是否满足性能和一致性要求；
- 某种部署方式是否支持目标规模；
- 外部 API 是否有关键限制；
- 数据迁移是否可以平滑完成。

这类内容应作为有边界的 investigation requirement，而不是直接假设一个答案。

## 3. 建立最小基础架构契约

使用 `engineering-foundation-design`，建立未来开发必须遵守的基础规则：

- 核心模块和职责；
- 依赖方向；
- 公共 API 或内部接口；
- 数据模型和持久化边界；
- 安全、权限和错误处理原则；
- 部署和运行环境；
- 关键性能或可靠性不变量；
- 测试和验证策略；
- 权威文档应该放在哪里。

这里的目标不是提前设计所有细节，而是让后续执行者不必重新决定：

- 哪个模块拥有某项能力；
- 哪些模块不能互相依赖；
- 哪些数据格式不能随意改变；
- 哪些边界属于公共契约；
- 哪些架构选择已经被固定。

应尽量保持基础设计薄，不要一开始就建立庞大的文档树、所有模块的详细设计或一个永久性的总计划。

## 4. 将大型项目拆成多个 Medium 需求

拆分时不要简单按“前端、后端、数据库、运维”分层。更好的拆法通常是按可验证的垂直结果拆分。

每个 Medium 单元应具备：

- 明确的可观察结果；
- 明确的范围和非目标；
- 真实的依赖；
- 可独立验证的验收行为；
- 所需的宏观固定决策；
- 明确的 Open 问题；
- 安全的中间状态。

通常第一个单元可以是一个最小 walking skeleton，即贯穿主要边界的薄切片，用来验证：

- 项目能否构建和运行；
- 核心模块边界是否合理；
- 数据流是否可行；
- 测试和部署路径是否成立；
- 关键技术假设是否正确。

之后再逐步增加完整业务能力、迁移能力、性能优化和运营能力。

## 5. 每个 Medium 单元独立走一遍交付流程

对于每个拆出的需求，按以下顺序处理：

### Specification

明确需求、约束、验收行为和接受的设计方向。

### Execution Planning

明确实施顺序、依赖、工作单元和验证方式。

### Implementation

执行经过授权的代码和配置修改。

### Review

同时检查：

- 目标行为是否实现；
- 是否破坏架构、契约和不变量；
- 是否引入回归；
- 是否扩大了范围；
- 是否产生不必要复杂度。

### Knowledge Governance

只有在确实产生长期有效的架构决策、契约、运行约束或文档更新需求时，才更新权威知识来源。

完成的临时计划不应自动变成永久文档。

## 6. 多 Agent 协作时再启用委派和交接

如果只由一个执行者完成某个阶段，不需要为了“看起来专业”而强行拆分。

如果需要多人或多 Agent 协作：

- 用 `engineering-plan-and-delegate` 决定如何拆解和分配；
- 用 `engineering-handoff` 在真实交接点传递目标、固定决策、证据、剩余工作和下一步；
- 不要只传递聊天记录或模糊任务描述。

交接内容必须区分：

- 已完成的工作；
- 已运行的检查及结果；
- 尚未验证的内容；
- 接收者可以自行决定的实现细节；
- 必须升级的架构或产品问题。

## 7. 推荐的整体阶段结构

一个从零开始的大型项目可以抽象成：

| 阶段 | 主要目的 | 主要 Skill |
|---|---|---|
| 目标澄清 | 将一句话扩展为宏观目标和边界 | `engineering-initiative-shaping` |
| 基础设计 | 固定架构边界、契约和不变量 | `engineering-foundation-design` |
| 风险调查 | 验证关键未知假设 | `engineering-investigation` |
| 阶段拆分 | 形成多个可独立交付的 Medium 单元 | `engineering-initiative-shaping` |
| 需求规格 | 明确某个阶段要实现什么 | `engineering-specification` |
| 执行计划 | 明确如何实现和验证 | `engineering-execution-planning` |
| 编码实现 | 修改代码和工程文件 | `engineering-implementation` |
| 阶段验收 | 判断结果是否真正可接受 | `engineering-review` |
| 知识维护 | 更新或收敛权威设计和契约 | `engineering-knowledge-governance` |
| 实际交接 | 跨执行者传递工作状态 | `engineering-handoff` |

核心原则是：先确定目的和基础边界，再拆分阶段；每个阶段独立规格化、实现和验收。不要把整个大型项目一次性展开成一份无法验证、无法维护的巨型实施计划。
