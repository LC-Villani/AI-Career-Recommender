# AI Career Recommender

A recommendation engine that suggests AI and backend projects based on a user's goals, skill level, and technical interests. 

As of March 31, 2026, this is the first version of the project.  
The current implementation does not yet include the AI-based recommendation layer, which will be added in future versions.

## Overview

This project was built as an initial prototype of a recommendation system focused on helping aspiring developers choose relevant projects for their portfolio and learning path.

It was inspired by a challenge that many people face, including myself: knowing what to build next and how to choose projects more strategically.

The current version uses a **rule-based scoring system** to compare a user's profile with a set of predefined project options and return the most compatible recommendations.

Even though this is still an early version, the goal is to gradually evolve it into a more intelligent recommendation system with stronger AI components.

## Why this project

Many people who want to enter AI, backend, or software engineering struggle with questions like:

- What kind of project should I build next?
- Which projects match my current level?
- What makes sense for my portfolio goals?
- How can I choose projects more strategically?

This project was created to explore that problem through a practical Python implementation.

## Current version

### Features
- User profile input through terminal
- Rule-based recommendation logic
- Score calculation based on:
  - current level
  - main goal
  - technical interests
  - preferred project duration
- Ranking of the most compatible projects
- Structured and expandable Python code

## Example input

- **Level:** intermediate
- **Goal:** international
- **Interests:** python, llm, backend
- **Preferred duration:** 2 weeks

## Example output

Recommended projects based on the user's profile, including:

- project title
- description
- level
- tags
- estimated duration
- compatibility score

## Tech stack

- Python
