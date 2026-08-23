 export interface Document {
  id: number;
  document_name: string;
  pages: number;
  chunks: number;
}

export interface UploadResponse {
  document: string;
  stored_as: string;
  status: string;
  ingestion: {
    document: string;
    pages: number;
    chunks: number;
  };
}