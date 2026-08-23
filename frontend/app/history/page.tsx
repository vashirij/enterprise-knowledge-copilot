export default function HistoryPage() {
  return (
    <main className="min-h-screen bg-gray-50">
      <div className="mx-auto max-w-5xl px-6 py-12">

        {/* Page Header */}
        <div className="mb-10">
          <h1 className="text-3xl font-semibold text-gray-950">
            Chat History
          </h1>

          <p className="mt-2 text-gray-600">
            Review previous Enterprise Knowledge Copilot conversations.
          </p>
        </div>

        {/* History Card */}
        <section className="rounded-2xl border border-gray-200 bg-white shadow-sm">

          <div className="border-b border-gray-200 px-6 py-4">
            <h2 className="font-semibold text-gray-900">
              Conversations
            </h2>
          </div>

          <div className="p-8">

            <div className="rounded-xl border border-dashed border-gray-300 bg-gray-50 p-10 text-center">

              <div className="text-3xl">
                💬
              </div>

              <h3 className="mt-4 text-base font-semibold text-gray-900">
                No conversations yet
              </h3>

              <p className="mx-auto mt-2 max-w-md text-sm leading-6 text-gray-500">
                Your saved Enterprise Knowledge Copilot conversations
                will appear here after chat history is connected.
              </p>

              <a
                href="/"
                className="mt-6 inline-flex rounded-xl bg-gray-950 px-5 py-3 text-sm font-medium text-white transition hover:bg-gray-800"
              >
                Start a conversation
              </a>

            </div>

          </div>

        </section>

      </div>
    </main>
  );
}