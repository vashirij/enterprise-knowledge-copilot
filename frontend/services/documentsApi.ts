import {
  Document,
  UploadResponse,
} from "@/types/document";

const API_URL =
  process.env.NEXT_PUBLIC_API_URL ??
  "http://127.0.0.1:8000";


export async function getDocuments(): Promise<Document[]> {

  const response = await fetch(
    `${API_URL}/api/v1/documents`
  );

  if (!response.ok) {
    throw new Error("Unable to load documents.");
  }

  return response.json();
}


export async function uploadDocument(
  file: File
): Promise<UploadResponse> {

  const formData = new FormData();

  formData.append("file", file);

  const response = await fetch(
    `${API_URL}/api/v1/documents/upload`,
    {
      method: "POST",
      body: formData,
    }
  );

  if (!response.ok) {
    throw new Error("Document upload failed.");
  }

  return response.json();
}


export async function deleteDocument(
  documentId: number
) {

  const response = await fetch(
    `${API_URL}/api/v1/documents/${documentId}`,
    {
      method: "DELETE",
    }
  );

  if (!response.ok) {
    throw new Error("Unable to delete document.");
  }

  return response.json();
}