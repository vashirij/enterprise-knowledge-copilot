"use client";

import { FormEvent, useState } from "react";

import SourceCard from "@/components/SourceCard";
import { askQuestion } from "@/services/chatApi";
import { AskResponse } from "@/types/chat";

export default function Home() {
  const [question, setQuestion] = useState("");
  const [result, setResult] = useState<AskResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function handleSubmit(
    event: FormEvent<HTMLFormElement>
  ) {
    event.preventDefault();

    const cleanQuestion = question.trim();

    if (!cleanQuestion) {
      return;
    }

    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const response = await askQuestion(cleanQuestion);
      setResult(response);
    } catch (error) {
      if (error instanceof Error) {
        setError(error.message);
      } else {
        setError("Unable to reach the Knowledge Copilot.");
      }
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="min-h-screen bg-gray-50">
      <div className="mx-auto max-w-4xl px-6 py-12">

        {/* Header */}
        <header className="mb-10">
          <p className="text-sm font-semibold uppercase tracking-wider text-blue-600">
            Enterprise AI
          </p>

          <h1 className="mt-2 text-4xl font-semibold text-gray-950">
            Enterprise Knowledge Copilot
          </h1>

          <p className="mt-3 max-w-2xl text-gray-600">
            Ask questions about enterprise documents and receive
            grounded answers with supporting sources.
          </p>
        </header>

        {/* Question Form */}
        <section className="rounded-2xl border border-gray-200 bg-white p-6 shadow-sm">
          <form onSubmit={handleSubmit} className="space-y-4">

            <label
              htmlFor="question"
              className="block font-medium text-gray-900"
            >
              Ask a question
            </label>

            <textarea
              id="question"
              value={question}
              onChange={(event) =>
                setQuestion(event.target.value)
              }
              placeholder="Example: Are sick days paid?"
              rows={4}
              className="w-full resize-none rounded-xl border border-gray-300 px-4 py-3 text-gray-900 outline-none transition focus:border-blue-500 focus:ring-2 focus:ring-blue-100"
            />

            <button
              type="submit"
              disabled={loading || !question.trim()}
              className="rounded-xl bg-gray-950 px-5 py-3 font-medium text-white transition hover:bg-gray-800 disabled:cursor-not-allowed disabled:opacity-50"
            >
              {loading ? "Searching..." : "Ask Copilot"}
            </button>

          </form>
        </section>

        {/* Error */}
        {error && (
          <div className="mt-6 rounded-xl border border-red-200 bg-red-50 p-4 text-red-700">
            {error}
          </div>
        )}

        {/* Result */}
        {result && (
          <section className="mt-8 space-y-6">

            {/* Answer */}
            <div className="rounded-2xl border border-gray-200 bg-white p-6 shadow-sm">
              <p className="text-sm font-semibold uppercase tracking-wide text-gray-500">
                Answer
              </p>

              <p className="mt-3 whitespace-pre-line text-lg leading-8 text-gray-900">
                {result.answer}
              </p>
            </div>

            {/* Sources */}
            {result.sources.length > 0 && (
              <div>
                <h2 className="mb-3 text-sm font-semibold uppercase tracking-wide text-gray-500">
                  Sources
                </h2>

                <div className="grid gap-3 md:grid-cols-2">
                  {result.sources.map((source, index) => (
                    <SourceCard
                      key={`${source.document}-${source.page}-${source.chunk_index}-${index}`}
                      source={source}
                    />
                  ))}
                </div>
              </div>
            )}

          </section>
        )}

      </div>
    </main>
  );
}