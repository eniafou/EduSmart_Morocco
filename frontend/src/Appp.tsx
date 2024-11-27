import React, { useState } from 'react';
import { Card } from './components/ui/card';
import { Button } from './components/ui/button';
import { Loader2 } from 'lucide-react';
import { marked } from 'marked';

const EssayEvaluationApp: React.FC = () => {
  const [essay, setEssay] = useState<string>('');
  const [evaluation, setEvaluation] = useState<string>('');
  const [isLoading, setIsLoading] = useState<boolean>(false);

  const evaluateEssay = async () => {
    setIsLoading(true);
    
    await new Promise(resolve => setTimeout(resolve, 2000));
    
    const mockEvaluation = `
# Essay Evaluation

## Overall Score: 85/100

### Content Analysis
- **Main Argument**: Strong and well-developed
- **Supporting Evidence**: Good use of examples
- **Logic Flow**: Clear progression of ideas

### Structure
- **Introduction**: Well-crafted (8/10)
- **Body Paragraphs**: Good organization (7/10)
- **Conclusion**: Effective summary (8/10)

### Language Usage
- **Grammar**: Few minor errors
- **Vocabulary**: Advanced and appropriate
- **Style**: Consistent academic tone

### Areas for Improvement
1. Consider adding more transitional phrases
2. Strengthen counter-arguments
3. Include more specific examples

### Strengths
1. Clear thesis statement
2. Strong analytical approach
3. Effective use of academic language
`;
    
    setEvaluation(mockEvaluation);
    setIsLoading(false);
  };

  return (
    <div className="flex h-screen bg-gray-100">
      <div className="w-1/2 p-6 flex flex-col">
        <Card className="flex-1 flex flex-col">
          <div className="p-4 border-b">
            <h2 className="text-xl font-bold">Write Your Essay</h2>
          </div>
          <textarea
            className="flex-1 p-4 resize-none focus:outline-none"
            placeholder="Start writing your essay here..."
            value={essay}
            onChange={(e) => setEssay(e.target.value)}
          />
          <div className="p-4 flex justify-center border-t">
            <Button 
              onClick={evaluateEssay} 
              disabled={!essay.trim() || isLoading}
              className="w-40"
            >
              {isLoading ? (
                <>
                  <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                  Evaluating...
                </>
              ) : (
                'Submit Essay'
              )}
            </Button>
          </div>
        </Card>
      </div>

      <div className="w-1/2 p-6">
        <Card className="h-full overflow-auto">
          <div className="p-4 border-b">
            <h2 className="text-xl font-bold">Evaluation Results</h2>
          </div>
          <div className="p-4 prose max-w-none">
            {evaluation ? (
              <div dangerouslySetInnerHTML={{ 
                __html: marked.parse(evaluation) 
              }} />
            ) : (
              <div className="text-gray-500 text-center mt-8">
                Submit your essay to see the evaluation results
              </div>
            )}
          </div>
        </Card>
      </div>
    </div>
  );
};

export default EssayEvaluationApp;