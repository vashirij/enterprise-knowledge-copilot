import type { Metadata } from "next";
import Link from "next/link";
import "./globals.css";

export const metadata: Metadata = {
  title: "Enterprise Knowledge Copilot",
  description: "Enterprise RAG knowledge assistant",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="bg-gray-50 text-gray-950">

        <div className="flex min-h-screen">

          {/* =========================
              SIDEBAR
          ========================== */}
          <aside className="flex w-64 shrink-0 flex-col border-r border-gray-200 bg-white text-gray-900">

            {/* Branding */}
            <div className="border-b border-gray-200 px-6 py-6">

              <p className="text-xs font-bold uppercase tracking-widest text-blue-600">
                Enterprise AI
              </p>

              <h1 className="mt-2 text-xl font-bold text-gray-950">
                Knowledge Copilot
              </h1>

              <p className="mt-1 text-xs text-gray-500">
                Enterprise Knowledge Assistant
              </p>

            </div>


            {/* Navigation */}
            <nav className="flex-1 space-y-2 p-4">

              <Link
                href="/"
                className="flex items-center gap-3 rounded-xl px-4 py-3 text-sm font-medium text-gray-700 transition hover:bg-gray-100 hover:text-gray-950"
              >
                <span>💬</span>
                <span>Chat</span>
              </Link>


              <Link
                href="/documents"
                className="flex items-center gap-3 rounded-xl px-4 py-3 text-sm font-medium text-gray-700 transition hover:bg-gray-100 hover:text-gray-950"
              >
                <span>📄</span>
                <span>Documents</span>
              </Link>


              <Link
                href="/history"
                className="flex items-center gap-3 rounded-xl px-4 py-3 text-sm font-medium text-gray-700 transition hover:bg-gray-100 hover:text-gray-950"
              >
                <span>🕘</span>
                <span>Chat History</span>
              </Link>

            </nav>


            {/* AI Status */}
            <div className="border-t border-gray-200 p-4">

              <div className="rounded-xl bg-gray-50 p-4">

                <p className="text-xs font-medium uppercase tracking-wide text-gray-500">
                  Local AI
                </p>

                <p className="mt-2 text-sm font-semibold text-gray-900">
                  Qwen 2.5 3B
                </p>

                <div className="mt-2 flex items-center gap-2">

                  <span className="h-2 w-2 rounded-full bg-green-500" />

                  <span className="text-xs font-medium text-green-700">
                    Ollama
                  </span>

                </div>

              </div>

            </div>

          </aside>


          {/* =========================
              MAIN APPLICATION
          ========================== */}
          <div className="flex min-w-0 flex-1 flex-col">

            {/* Top bar */}
            <header className="flex h-16 items-center justify-between border-b border-gray-200 bg-white px-6">

              <div>
                <p className="text-sm font-medium text-gray-700">
                  Enterprise Knowledge Copilot
                </p>
              </div>

              <div className="flex items-center gap-2">

                <span className="h-2 w-2 rounded-full bg-green-500" />

                <span className="text-xs text-gray-500">
                  System Ready
                </span>

              </div>

            </header>


            {/* Page content */}
            <main className="min-w-0 flex-1 overflow-auto">
              {children}
            </main>

          </div>

        </div>

      </body>
    </html>
  );
}