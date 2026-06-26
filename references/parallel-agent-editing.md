# 并行Agent编辑

多Agent同时编辑同一项目，如何避免冲突？

## 分工原则

1. **文件级隔离**：每个 Agent 负责不同文件（如 Agent A 改 .md，Agent B 改 .py）
2. **章节级隔离**：同一文件的不同章节分给不同 Agent
3. **只读共享**：共享的配置文件/依赖清单设为只读，统一由一个 Agent 管理

## 冲突处理

- **合并冲突**：用 git merge，人工review差异
- **依赖冲突**：统一版本号管理（如 requirements.txt 由一个Agent维护）
- **格式冲突**：统一 .editorconfig 或格式化脚本

## 最佳实践

- 每次编辑前 `git pull`
- 每次编辑后 `git commit + push`（小步提交）
- 每天同步一次进度（避免分叉过大）

## 参考

- Git 协作：https://git-scm.com/book/en/v2
