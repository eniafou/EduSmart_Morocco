export type QCMData = Array<{
    sous_cours_name: string;
    content: Array<{
      question: string;
      options: string[];
      correct_answer: string;
    }>;
  }>;