"use client";

import {
  ChangeEvent,
  useEffect,
  useState,
} from "react";

import {
  deleteDocument,
  getDocuments,
  uploadDocument,
} from "@/services/documentsApi";

import { Document } from "@/types/document";


export default function DocumentsPage() {

  const [documents, setDocuments] =
    useState<Document[]>([]);

  const [selectedFile, setSelectedFile] =
    useState<File | null>(null);

  const [loading, setLoading] =
    useState(false);

  const [message, setMessage] =
    useState<string | null>(null);


  async function loadDocuments() {

    try {
      const data = await getDocuments();
      setDocuments(data);
    } catch {
      setMessage(
        "Unable to load documents."
      );
    }
  }


  useEffect(() => {
    loadDocuments();
  }, []);


  function handleFileChange(
    event: ChangeEvent<HTMLInputElement>
  ) {

    const file =
      event.target.files?.[0];

    setSelectedFile(file ?? null);
  }


  async function handleUpload() {

    if (!selectedFile) {
      return;
    }

    setLoading(true);
    setMessage(null);

    try {

      const result =
        await uploadDocument(selectedFile);

      setMessage(
        `${result.document} uploaded successfully.`
      );

      setSelectedFile(null);

      await loadDocuments();

    } catch {
      setMessage(
        "Unable to upload document."
      );
    } finally {
      setLoading(false);
    }
  }


  async function handleDelete(
    documentId: number
  ) {

    const confirmed =
      window.confirm(
        "Delete this document?"
      );

    if (!confirmed) {
      return;
    }

    try {

      await deleteDocument(documentId);

      await loadDocuments();

    } catch {
      setMessage(
        "Unable to delete document."
      );
    }
  }


  return (
    <main className="min-h-screen bg-gray-50">

      <div className="mx-auto max-w-5xl px-6 py-12">

        <div className="mb-10">

          <a
            href="/"
            className="text-sm text-blue-600 hover:underline"
          >
            ← Knowledge Copilot
          </a>

          <h1 className="mt-4 text-3xl font-semibold text-gray-950">
            Documents
          </h1>

          <p className="mt-2 text-gray-600">
            Upload and manage enterprise knowledge sources.
          </p>

        </div>


        {/* Upload */}

        <section className="mb-8 rounded-2xl border border-gray-200 bg-white p-6 shadow-sm">

          <h2 className="text-lg font-semibold text-gray-900">
            Upload document
          </h2>

          <div className="mt-4 flex flex-col gap-4 sm:flex-row sm:items-center">

            <input
              type="file"
              accept=".pdf,application/pdf"
              onChange={handleFileChange}
              className="block text-sm text-gray-700"
            />

            <button
              onClick={handleUpload}
              disabled={
                !selectedFile ||
                loading
              }
              className="rounded-xl bg-gray-950 px-5 py-3 text-sm font-medium text-white disabled:opacity-50"
            >
              {loading
                ? "Processing..."
                : "Upload"}
            </button>

          </div>

          {message && (
            <p className="mt-4 text-sm text-gray-600">
              {message}
            </p>
          )}

        </section>


        {/* Documents */}

        <section className="rounded-2xl border border-gray-200 bg-white shadow-sm">

          <div className="border-b border-gray-200 px-6 py-4">

            <h2 className="font-semibold text-gray-900">
              Knowledge sources
            </h2>

          </div>


          {documents.length === 0 ? (

            <div className="p-8 text-center text-gray-500">
              No documents uploaded.
            </div>

          ) : (

            <div className="divide-y divide-gray-100">

              {documents.map(
                (document) => (

                  <div
                    key={document.id}
                    className="flex items-center justify-between gap-6 p-6"
                  >

                    <div>

                      <p className="font-medium text-gray-900">
                        {document.document_name}
                      </p>

                      <p className="mt-1 text-sm text-gray-500">
                        {document.pages} pages
                        {" · "}
                        {document.chunks} chunks
                      </p>

                    </div>


                    <button
                      onClick={() =>
                        handleDelete(
                          document.id
                        )
                      }
                      className="rounded-lg border border-red-200 px-3 py-2 text-sm font-medium text-red-600 hover:bg-red-50"
                    >
                      Delete
                    </button>

                  </div>

                )
              )}

            </div>

          )}

        </section>

      </div>

    </main>
  );
}