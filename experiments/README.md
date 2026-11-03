# 实验清单约定

每章一份实测记录：`experiments/chNN.md`（`NN` 为两位章号，如 `ch03.md`）。

## 每份清单至少包含

- 章号与项目名
- 要跑的命令（完整路径或相对本仓库根）
- 输入（若交互：写明 `printf` 喂入内容）
- 期望输出（关键行即可）
- 实测日期（Asia/Shanghai）
- 实测结果：通过 / 失败及备注

## 规则

- 命令先实测再写进章稿
- 无显示器环境对 turtle 等可用 `python3 -m py_compile`，并注明需本机窗口运行
- 批测汇总可另建 `experiments/batch-smoke.md`（全书联校阶段）
