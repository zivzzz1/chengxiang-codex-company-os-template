---
name: one-image-understanding
description: Use for 一张图看懂, infographics, structure maps, capability maps, workflow diagrams, or decision diagrams where the final output should be one standalone generated image.
---

# One Image Understanding

Use this skill when the user asks for `一张图看懂`, `信息图`, `结构图`, `能力地图`, `流程图`, or similar.

Rules:

1. The final image must be a standalone generated bitmap.
2. Text should be generated inside the image, not overlaid afterward.
3. Do not satisfy this request with HTML cards, SVG, screenshots, or Mermaid unless the user explicitly changes route.
4. If image generation is unavailable, output a prompt and structure, and clearly say the image was not generated.
