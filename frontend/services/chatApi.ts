import { AskResponse } from "@/types/chat";

const API_URL =
  process.env.NEXT_PUBLIC_API_URL ?? "http://127.0.0.1:8000";

export async function askQuestion(
  question: string
): Promise<AskResponse> {
  const response = await fetch(`${API_URL}/api/v1/ask`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ question }),
  });

  if (!response.ok) {
    throw new Error("Unable to process question.");
  }

  return response.json();
}