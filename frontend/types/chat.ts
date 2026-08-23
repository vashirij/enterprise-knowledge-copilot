export interface Source {
  document: string;
  page: number;
  chunk_index: number;
  rerank_score: number;
}

export interface AskResponse {
  question: string;
  answer: string;
  sources: Source[];
}