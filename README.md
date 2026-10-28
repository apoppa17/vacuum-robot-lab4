# Vacuum Robot Reinforcement Learning - Lab 4

## Project Overview

This repository contains the context engineering configuration for a vacuum robot reinforcement learning project. The robot will eventually use Q-learning to navigate a 4x4 grid environment.

The purpose of Lab 4 is to configure context engineering strategies 1 and 4 before implementing the learning algorithm.

## Project Structure

- `CLAUDE.md` - Contains project instructions, environment details, and development guidelines.
- `.claude/agents/code-reviewer.md` - Defines a specialized sub-agent for reviewing future Python implementations.
- `README.md` - Documents the repository structure and context engineering strategies.

## Context Engineering Strategies

### Strategy 1: Persistent Memory

The `CLAUDE.md` file provides Claude Code with project information that can be reused across sessions. This includes the grid environment, project goal, and coding guidelines.

### Strategy 4: Context Isolation

The Code Reviewer sub-agent is responsible for checking code correctness, readability, and compliance with project requirements. It operates with its own context and has access to read-only tools.
