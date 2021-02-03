# Hello Internet AI
![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)
![TensorFlow Requirement: 1.x](https://img.shields.io/badge/TensorFlow%20Requirement-1.x-brightgreen)
![Commit Activity](https://img.shields.io/github/last-commit/stevend94/CoNLL2020?color=blue)
![Complete](https://img.shields.io/badge/Complete-90%25-green)

![alt text](https://b.thumbs.redditmedia.com/UnXpHrwhF5dO-XtAw5hTmHm5L6R73YdjPDpXVPTj5Lg.png)

&nbsp;

# General Information:
### This repository contains labelled transcripts for all [HelloInternet](http://www.hellointernet.fm/) podcast episodes. It also contains code that allows the user to train their own Neural Network that can generate transcripts of their own. 

&nbsp;

# Data
### All the data is available to download. Data was extracted using otter.ai along with some manual labels. You can download the raw data or the processed data below.
* [Raw manuscripts with time stamps](https://drive.google.com/file/d/1lBOr_SCnv-EsB9KSTh0JV2owg6815U7a/view?usp=sharing)
* [Text data](https://drive.google.com/file/d/1qHQfDa2pr6f8ZtedK8hsrwcoStayoE6b/view?usp=sharing)

### Right now the data isn't very clean, but we may look in the future to employ some lexical resources and preprocessing to create cleaner text data.

&nbsp;

# GPT2
### Models were trained using [gpt-2-simple](https://github.com/minimaxir/gpt-2-simple) which requires tensorflow to run. Check out there great repository for more details. More instructions are provided in the gpt-2-simple folder on how to train your own model. We also provide a checkpoint for a GPT2 1.5B parameter model trained on this data for 10000 steps [HERE](https://drive.google.com/file/d/1x3R_oFZpnDS0oCipePofoxtgM8-7elQl/view?usp=sharing) (WARNING MODEL IS SEVERAL GB IN SIZE). To use this model, we recommend using a much larger machine, perhaps on google cloud or google collab.

&nbsp;

# EDA
### We also provide a simple notebook for exploring the data, and may add an extra notebook that solves some other task (For example, predicting which person is talking).

&nbsp;

# Example from transcripts generated from GPT-2 124M model.

```txt
[Grey] Brady no more plane crash corner. Yeah,
[Brady] yeah. But But yeah, we've got plane crash corner on the internet.
[Grey] It's plane crash corner, right?
[Brady] Well, I mean, if you say something plane crash corner, you go. Okay, well,
[Grey] I went on the internet to see the website and I got that Brady's paper cut not that I've got not that I've got paper cuts internet
[Brady] I have gone on the internet. And I got the link to this article about plane crash corner. I'm looking at it straight away. And I'm like, okay, all right, but it's not plane crash corner. I went looking for it. And I haven't come across it. I went looking for it on the internet. But no one has seen it. And I was like, No, no one has. But somebody has.
[Grey] This is why I was like a little bit terrified when the article came out. Because I don't know who this is. This is just this is what this is. This is the internet. This is what the internet is. It's the world's premier source of news. It's the source of all of the internet's news. So I was like, Okay, I'm gonna warn you. I'm going to warn you. I'm not going to tell you that. But I did pull out my iPhone and saw this article that you'd probably seen before. It's about this incident that ended up getting me into a plane. And it's about this incident that took the life of this pilot, who was doing the finding of the plane. And he says he did not panic or call for help or apologize or explain what was going on. Instead, he says he crashed the plane as the search and rescue efforts go on. And it's just like this, this amazing, amazing thing. And I just came away from this article thinking, wow, I'm glad people are aware of this. Even though I don't know nothing about this, and I don't know what happened, I was just so outraged by this thing that I was like, I don't know, I just I don't want to know who it was. I don't want to know what caused or the way it happened. And I was like, wow, it was amazing. I can't believe that you know, this is the first time I've ever heard about a plane crash. So I'm like, Oh, I can't believe it. And I was like, What the heck are you talking about? And I was like, I'm just reading this article. And it's like, oh, it's totally amazing.
[Brady] I don't know. I just find it very strange. And I don't know if you're out of the plane, but I mean, I don't even know what happened. Like, I don't know, I'm perfectly okay with it. There's no like, problems. No, no problems at all.
[Grey] I'm a little bit worried about this because when I saw this article, and I saw that it was about plane crash corner, I was like, oh my goodness, what is this? It's about plane crash corner?
[Brady] Well, I mean, this is this is where we are now. Like, we're more aware of it, because we just got this big story that got me into a few other websites about a plane crash that happened a few weeks ago. But I mean, this is a story of the very, very, very early days of our careers. So it's like, I don't know, I don't know how things work in advertising. I guess I don't know what happened. But I don't know. I'm not sure how it works. Like, I don't know anything about it. I don't know. I think it's probably a bit of a mystery to me how it works. And I don't know what caused it, or how long it's been a mystery to me. I don't know. I just don't know. What's the point of mystery to me? Why is a mystery?
[Grey] I know.
[Brady] It's not a mystery. What's the point of mystery? Why is it a mystery is to be a bit suspicious of what's going on? Because it's like, you know, it's like a bit of a mystery. Okay, why is this mystery? I mean, it's not like, I think, you know, it's not like, I've seen a couple of interesting things in it, but this is just like, it's not like a mystery. What's going on? They're not like, Oh, like, you know, you know, I'm not a big fan of the new

```