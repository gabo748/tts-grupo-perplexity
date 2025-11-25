# Research: OpenAI Whisper API Integration

**Date**: 2025-11-24
**Feature**: [Text-to-Speech and Translation CLI](../spec.md)

## Objective

To determine how to integrate with the OpenAI Whisper API for a personal CLI tool, focusing on API key usage and the pricing model, as per the initial user request.

## Findings

A web search was conducted to understand the pricing and usage model for the OpenAI Whisper API. While specific search results were not retrieved during this session, standard OpenAI API practices can be applied.

### Decision: Use Standard OpenAI API with Usage-Based Billing

The integration will proceed assuming the following:

1.  **API Key**: A standard OpenAI API key, provided via an environment variable (`OPENAI_API_KEY`), will be used to authenticate with the API. There is no special "Whisper-only" key.
2.  **Pricing Model**: The Whisper model is part of OpenAI's standard API offerings. The pricing is usage-based, calculated per minute of audio processed for both transcription (speech-to-text) and translation. The text-to-speech (TTS) model has its own pricing, which is per 1,000 characters.
3.  **"Freemium" Model**: There is no distinct "freemium" API endpoint. The concept of "freemium" typically relates to a free credit tier that new OpenAI accounts receive. The API itself is the same regardless of whether the user is on a free trial or a paid plan. The tool will use the provided API key, and any costs incurred will be billed to the associated OpenAI account.

## Rationale

This approach is the standard method for using OpenAI APIs. It aligns with the user's clarification that this is a personal project and the API key will be managed via an environment variable, implying acceptance of potential costs. The tool's responsibility is to use the key to make API calls, and the user's responsibility is to manage the key and its associated billing.

## Alternatives Considered

- **Searching for a separate "free" API**: This was ruled out as OpenAI does not typically offer separate, feature-limited free APIs. The free offering is almost always in the form of initial credits.
