# KaaS AI Service Documentation

## Overview

KaaS (Knowledge as a Service) AI Service is the intelligence layer of the learning platform.

It provides:

* Personalized AI tutoring
* Knowledge-based question answering
* Course recommendation
* Learner personalization
* Future AI assessment generation
* AI mentor capabilities

The AI service follows a modular architecture where each AI capability has its own responsibility.

---

# AI Service Architecture

```
                    KaaS Platform

                         |
                         |

                  AI Service Layer


                         |

 -------------------------------------------------
 |                 |                 |             |
 |                 |                 |             |

 RAG AI Tutor   Recommendation   Assessment    AI Agents

 |                 |                 |
 |                 |                 |

Knowledge       User Data        Learner Data

Documents       Courses          Skills

Vector DB       History          Performance


                         |

                         |

                     Groq LLM

                         |

                         |

              Personalized AI Output
```

---

# 1. AI Tutor (RAG System)

## Purpose

AI Tutor allows learners to ask questions and receive answers based on KaaS learning content.

Instead of directly asking an LLM, the system first retrieves relevant knowledge from internal documents.

This prevents incorrect answers and keeps responses domain-specific.

---

# What is RAG?

RAG = Retrieval Augmented Generation

It combines:

1. Retrieval
2. Generation

Example:

User:

```
How does supervised learning work?
```

Flow:

```
User Question

      |

      ↓

Embedding Creation

      |

      ↓

Vector Database Search

      |

      ↓

Relevant Course Knowledge

      |

      ↓

Groq LLM

      |

      ↓

Final Answer
```

---

## Folder Structure

```
rag/

├── documents/

│     machine_learning.txt


├── splitter.py


├── embeddings.py


├── vector_store.py


├── retriever.py


└── test_vector_store.py
```

---

## File Responsibilities

### splitter.py

Purpose:

Break large documents into smaller chunks.

Example:

Before:

```
Machine Learning is a large topic...
```

After:

```
Chunk 1:
Introduction

Chunk 2:
Supervised Learning

Chunk 3:
Applications
```

Why?

Embedding models work better with smaller meaningful pieces.

---

### embeddings.py

Purpose:

Convert text into numerical vectors.

Example:

Text:

```
Machine Learning
```

Converted:

```
[0.234,0.541,0.123....]
```

These vectors allow similarity search.

---

### vector_store.py

Purpose:

Store embeddings.

Technology:

* FAISS

Flow:

```
Document

 ↓

Embedding

 ↓

FAISS Index

 ↓

Search
```

---

### retriever.py

Purpose:

Find relevant knowledge.

Example:

Question:

```
Explain reinforcement learning
```

Retrieves:

```
Reinforcement learning section
```

---

# 2. Personalized AI Chat

## Purpose

The AI explains concepts according to learner profile.

Example:

User:

```
USR000001
```

Database:

```
Role:
Trainer

Domain:
Data Science

Level:
Intermediate

Learning Style:
Reading
```

AI response changes according to learner.

---

## Architecture

```
User ID

   |

users.csv

   |

Learner Profile

   |

Groq Prompt

   |

Personalized Answer

```

---

# 3. Recommendation AI

## Purpose

Recommend courses based on:

* User interest
* Skill level
* Previous learning
* Course popularity

---

## Architecture

```
                 User


                  |

                  |


          User Profile


                  |

                  |


        Learning History


                  |

                  |


       Recommendation Engine


                  |

                  |

          Top Courses


                  |

                  |

              Groq AI


                  |

                  |

       Explanation Generation

```

---

## Folder Structure

```
recommendation/


├── recommender.py


├── history.py


├── personalized_recommender.py


├── groq_explainer.py


├── personalized_ai_recommendation.py


└── tests/
```

---

# File Explanation

## recommender.py

Basic course filtering.

Uses:

```
domain
level
status
```

Example:

```
Data Science
+
Intermediate

↓

Data Science Intermediate Courses
```

---

## history.py

Reads learner activity.

Tracks:

* Completed courses
* Current courses
* Scores

Example:

```
Completed:

CRS011988


In Progress:

CRS005119
```

---

## personalized_recommender.py

Combines:

```
Profile

+

History

+

Courses

```

Removes:

* Already completed courses
* Already enrolled courses

---

## groq_explainer.py

Uses Groq LLM.

Purpose:

Explain why a course is recommended.

Example:

Before:

```
Course A
```

After:

```
This course is recommended because
you are learning Data Science and your
current level is Intermediate.
```

---

## personalized_ai_recommendation.py

Final pipeline.

```
Database

   |

Recommendation Engine

   |

Groq Explanation

   |

Final AI Recommendation

```

---

# 4. Future AI Assessment Generator

## Purpose

Generate quizzes automatically based on learner weakness.

Architecture:

```
Learner Knowledge Gap

          |

          |

      Question Generator

          |

          |

        Groq LLM

          |

          |

       Quiz Creation

          |

          |

      Evaluation

          |

          |

    Skill Update

```

---

# 5. AI Curriculum Generator

## Purpose

Instructor provides:

```
Create LLMOps course
```

AI generates:

```
Course

 |

Modules

 |

Lessons

 |

Assessment

```

Architecture:

```
Instructor Input

       |

       |

     Groq LLM

       |

       |

Course Blueprint

       |

       |

Database

```

---

# 6. AI Mentor Agent

## Purpose

Monitor learner behaviour.

Example:

Learner watches same video section 3 times.

System:

```
Replay Detection

       |

       |

Knowledge Gap Created

       |

       |

Alternative Explanation

       |

       |

Notification

```

---

# 7. Predictive Learning Analytics

## Purpose

Detect dropout risk.

Input:

```
Login frequency

Course progress

Assessment score

Learning streak

```

Output:

```
Low Risk

Medium Risk

High Risk
```

---

# Complete KaaS AI Roadmap

```
                 KaaS AI Brain


                       |

 ------------------------------------------------

 |              |              |               |

RAG        Recommendation   Assessment     AI Agents


 |              |              |

Knowledge     Courses       Quizzes

Answer        Suggestion    Evaluation


                       |

                       |

                    Groq LLM


                       |

                       |

              Personalized Learning
```

---

# Current Completion Status

| Module                 | Status    |
| ---------------------- | --------- |
| RAG AI Tutor           | Completed |
| Personalized Chat      | Completed |
| Recommendation Engine  | Completed |
| Groq Explanation Layer | Completed |
| AI Assessment          | Pending   |
| Curriculum Generator   | Pending   |
| AI Mentor Agent        | Pending   |
| Dropout Prediction     | Pending   |

---

# Technology Stack

## AI

* Groq LLM
* Sentence Transformers
* Vector Embeddings
* FAISS

## Backend

* Python
* FastAPI

## Data

* CSV datasets
* Vector Database

## Architecture Principle

Each module has a single responsibility:

```
Data Layer

↓

AI Logic Layer

↓

API Layer

↓

Frontend
```

This keeps KaaS AI scalable and production-ready.

