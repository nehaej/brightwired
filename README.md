# Brightwired 
BrightWired is a sensory-friendly productivity and learning toolkit designed to reduce cognitive overload. It combines an adaptive text summarizer, low-stress planning tools, and a motivation assistant to help students start and sustain focused work. The project was built with neurodivergent learners in mind, including students with ADHD, dyslexia, and general concentration challenges.

## Why 
Many productivity and learning tools focus on sustained attention, quick reading, and frequent context-switching. For students with ADHD, dyslexia, or executive dysfunction, these ideas can make even simple tasks seem overwhelming. Instead of easing the process, current tools often add to the stress by fragmenting workflow across multiple platforms, complicated interfaces, and strict productivity systems. Most standard tools also assume linear thinking patterns, which can further disadvantage neurodivergent learners. 

## Gaps in Existing Tools 
- Prioritizes aesthetics over functional cognitive accessibility 
- Assumes consistent motivation, focus, and energy levels 
- Fragments workflows across multiple tabs and applications 
- Overly cluttered interfaces that increase sensory and cognitive load 
- Summarization tools that enforce a single tone or style rather than adapting to speciifc student needs 
BrightWired aims to bridge these gaps by priortising a utility first, minimalist UI, non fragemented workflow, and features designed specifically for cognitive accessiblity and task initiation. 

## Design Philosphy 
BrightWired follows three core principles:

- **Cognitive accessibility over visual complexity**  
- **Support for starting tasks, not just tracking them**  
- **Flexible, adaptive assistance instead of rigid productivity systems**

The project treats focus as a variable state rather than a fixed expectation, and designs around that reality.

## Feedback
BrightWired was pilot-tested with approximately 40 to 50 who self-identified as experiencing focus-related or academic challenges. Their feedback shaped the emphasis on low-stimulation design and flexible, non-linear task support. 
- Timer acceleration bug: Multiple users accidentally clicked the timer start button more than once, causing the timer to speed up. This led to the implementation of clearInterval() in the JavaScript frontend.
- Fragmented text tools: The initial version separated summarization and stylistic rephrasing into two different tools. Testers reported switching between tools increased friction and cognitive load.
- Tool consolidation: Based on this feedback, both features were merged into a single adaptive text tool that supports simplified summaries with flexible tone and structure.
  
## The Final Product
After changes were implemented, errors fixed, these were the general opinions of that testers:
- The summarization tool effectively translated dense academic material into clearer, more accessible explanations, particularly for students with attention or reading difficulties.
- The 25 min pomodoro timer helped students study in controlloed chunks without being overwhelmed by material
- Enco Bot was also said to be useful, and a good source of motivation



