import Link from 'next/link'
import { ArrowLeft, ExternalLink, FileText, Upload, ArrowRight } from 'lucide-react'
import { Button } from '@/components/ui/button'

const classData: Record<
  string,
  {
    name: string
    code: string
    description: string
    cheatsheets: Array<{
      id: string
      title: string
      type: 'pdf' | 'external'
      url?: string
      uploadDate?: string
    }>
  }
> = {
  'data-structures': {
    name: 'Data Structures',
    code: 'CS 2114',
    description: 'Comprehensive notes on algorithms, trees, graphs, and complexity analysis',
    cheatsheets: [
      {
        id: '1',
        title: 'My Notes - P1',
        type: 'pdf',
        uploadDate: '2025-12-08',
        url: 'https://files.bkmcoding.com/ds-sheetp1.pdf',
      },
      {
        id: '2',
        title: 'My Notes - P2',
        type: 'pdf',
        uploadDate: '2025-12-08',
        url: 'https://files.bkmcoding.com/ds-sheetp2.pdf',
      },
      {
        id: '3',
        title: 'Binary Trees & Traversal Methods',
        type: 'pdf',
        uploadDate: '2025-12-08',
        url: 'https://files.bkmcoding.com/ds-traversal.pdf',
      },
      {
        id: '3',
        title: 'Comprehensive Sorts',
        type: 'pdf',
        uploadDate: '2025-12-16',
        url: 'https://files.bkmcoding.com/ds-sorts.pdf',
      },
      {
        id: '4',
        title: 'VisuAlgo - Algorithm Visualizations',
        type: 'external',
        url: 'https://visualgo.net',
      },
      {
        id: '5',
        title: 'HelloAlgo - Concise Online Book',
        type: 'external',
        url: 'https://www.hello-algo.com/en/',
      },
      {
        id: '6',
        title: 'LeetCode Practice Problems',
        type: 'external',
        url: 'https://leetcode.com/problemset/',
      },
      {
        id: '7',
        title: 'Big-O Cheat Sheet',
        type: 'external',
        url: 'https://www.bigocheatsheet.com/',
      },
      {
        id: '8',
        title: 'Data Structure Visualizations - USFCA',
        type: 'external',
        url: 'https://www.cs.usfca.edu/~galles/visualization/Algorithms.html',
      },
    ],
  },
  'machine-learning': {
    name: 'Machine Learning',
    code: 'CS 3203',
    description: 'Neural networks, optimization, and model evaluation frameworks',
    cheatsheets: [
      {
        id: '1',
        title: 'Neural Network Architectures',
        type: 'pdf',
        uploadDate: '2025-12-08',
        url: 'https://files.bkmcoding.com/ml-neuralNetwork_arch.pdf',
      },
      {
        id: '2',
        title: 'Scikit-Learn Documentation',
        type: 'external',
        url: 'https://scikit-learn.org/stable/',
      },
      {
        id: '3',
        title: 'TensorFlow Official Tutorials',
        type: 'external',
        url: 'https://www.tensorflow.org/tutorials',
      },
      {
        id: '4',
        title: 'PyTorch Documentation',
        type: 'external',
        url: 'https://pytorch.org/docs/stable/index.html',
      },
      {
        id: '5',
        title: 'Kaggle Learn - Machine Learning',
        type: 'external',
        url: 'https://www.kaggle.com/learn/intro-to-machine-learning',
      },
      {
        id: '6',
        title: 'Machine Learning Crash Course - Google',
        type: 'external',
        url: 'https://developers.google.com/machine-learning/crash-course',
      },
      {
        id: '7',
        title: 'Papers With Code',
        type: 'external',
        url: 'https://paperswithcode.com/',
      },
      {
        id: '8',
        title: 'Deep Learning Book - Goodfellow et al.',
        type: 'external',
        url: 'https://www.deeplearningbook.org/',
      },
      {
        id: '9',
        title: 'Fast.ai Practical Deep Learning',
        type: 'external',
        url: 'https://course.fast.ai/',
      },
      {
        id: '10',
        title: 'Stanford CS229 ML Course',
        type: 'external',
        url: 'https://cs229.stanford.edu/',
      },
    ],
  },
  'linear-algebra': {
    name: 'Linear Algebra',
    code: 'MATH 3003',
    description: 'Vector spaces, transformations, eigenvalues and matrix operations',
    cheatsheets: [
      {
        id: '1',
        title: 'Matrix Operations Reference',
        type: 'pdf',
        uploadDate: '2025-12-08',
        url: 'https://files.bkmcoding.com/la-matrix-op.pdf',
      },
      {
        id: '2',
        title: '3Blue1Brown - Essence of Linear Algebra',
        type: 'external',
        url: 'https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab',
      },
      {
        id: '3',
        title: 'MIT OpenCourseWare - Linear Algebra',
        type: 'external',
        url: 'https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/',
      },
      {
        id: '4',
        title: 'Khan Academy Linear Algebra',
        type: 'external',
        url: 'https://www.khanacademy.org/math/linear-algebra',
      },
      {
        id: '5',
        title: 'Linear Algebra - Jim Hefferon (Free Textbook)',
        type: 'external',
        url: 'https://joshua.smcvt.edu/linearalgebra/',
      },
      {
        id: '6',
        title: 'Interactive Linear Algebra Textbook',
        type: 'external',
        url: 'https://textbooks.math.gatech.edu/ila/',
      },
      {
        id: '7',
        title: 'Matrix Cookbook',
        type: 'external',
        url: 'https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf',
      },
      {
        id: '8',
        title: "Paul's Online Math Notes - Linear Algebra",
        type: 'external',
        url: 'https://tutorial.math.lamar.edu/Classes/LinAlg/LinAlg.aspx',
      },
    ],
  },
  cybersecurity: {
    name: 'Cybersecurity',
    code: 'CS 2413',
    description: 'Network security, cryptography, penetration testing and threat analysis',
    cheatsheets: [
      {
        id: '1',
        title: 'My Notes',
        type: 'pdf',
        uploadDate: '2025-12-08',
        url: 'https://files.bkmcoding.com/cyber-sheet1.pdf',
      },
      {
        id: '2',
        title: 'OWASP Top 10 Security Risks',
        type: 'external',
        url: 'https://owasp.org/www-project-top-ten/',
      },
      {
        id: '3',
        title: 'Hack The Box - Practice Platform',
        type: 'external',
        url: 'https://www.hackthebox.com/',
      },
      {
        id: '4',
        title: 'TryHackMe - Interactive Labs',
        type: 'external',
        url: 'https://tryhackme.com/',
      },
      {
        id: '5',
        title: 'Cybrary - Free Security Courses',
        type: 'external',
        url: 'https://www.cybrary.it/',
      },
      {
        id: '6',
        title: 'NIST Cybersecurity Framework',
        type: 'external',
        url: 'https://www.nist.gov/cyberframework',
      },
      {
        id: '7',
        title: 'PortSwigger Web Security Academy',
        type: 'external',
        url: 'https://portswigger.net/web-security',
      },
      {
        id: '8',
        title: 'CyberSeek Career Pathways',
        type: 'external',
        url: 'https://www.cyberseek.org/pathway.html',
      },
      {
        id: '9',
        title: 'SANS Reading Room - Free Papers',
        type: 'external',
        url: 'https://www.sans.org/white-papers/',
      },
      {
        id: '10',
        title: 'Krebs on Security - News & Analysis',
        type: 'external',
        url: 'https://krebsonsecurity.com/',
      },
      {
        id: '11',
        title: 'Cryptography I - Stanford (Coursera)',
        type: 'external',
        url: 'https://www.coursera.org/learn/crypto',
      },
      {
        id: '12',
        title: 'PentesterLab - Hands-on Practice',
        type: 'external',
        url: 'https://pentesterlab.com/',
      },
    ],
  },
  'calc-iii': {
    name: 'Calculus III',
    code: 'MATH 3404',
    description: 'Multivariable calculus, partial derivatives, and vector calculus',
    cheatsheets: [
      {
        id: '1',
        title: 'My Notes',
        type: 'pdf',
        uploadDate: '2025-12-08',
        url: 'https://files.bkmcoding.com/calcIII-sheet1.pdf',
      },
      {
        id: '2',
        title: "Paul's Online Math Notes - Calc III",
        type: 'external',
        url: 'https://tutorial.math.lamar.edu/Classes/CalcIII/CalcIII.aspx',
      },
      {
        id: '3',
        title: 'MIT OpenCourseWare - Multivariable Calculus',
        type: 'external',
        url: 'https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/',
      },
      {
        id: '4',
        title: '3Blue1Brown - Multivariable Calculus',
        type: 'external',
        url: 'https://www.youtube.com/playlist?list=PLSQl0a2vh4HC5feHa6Rc5c0wbRTx56nF7',
      },
      {
        id: '5',
        title: 'Calculus III - LibreTexts',
        type: 'external',
        url: 'https://math.libretexts.org/Bookshelves/Calculus/Calculus_(OpenStax)',
      },
      {
        id: '6',
        title: 'WolframAlpha - Computation Engine',
        type: 'external',
        url: 'https://www.wolframalpha.com/',
      },
      {
        id: '7',
        title: 'GeoGebra 3D Calculator',
        type: 'external',
        url: 'https://www.geogebra.org/3d',
      },
      {
        id: '8',
        title: 'Professor Leonard - Calc III Lectures',
        type: 'external',
        url: 'https://www.youtube.com/playlist?list=PLDesaqWTN6ESk16YRmzuJ8f6-rnuy0Ry7',
      },
      {
        id: '9',
        title: 'Symbolab - Step-by-Step Solutions',
        type: 'external',
        url: 'https://www.symbolab.com/',
      },
    ],
  },
  TBD: {
    name: 'To be Determined',
    code: 'TEMP 0001',
    description: "Yeah there would be info right here but this isn't a class.",
    cheatsheets: [
      {
        id: '1',
        title: 'What did you expect in here.',
        type: 'external',
        url: 'https://msheet.bkmcoding.com',
      },
      {
        id: '2',
        title: 'Go back.',
        type: 'external',
        url: 'https://msheet.bkmcoding.com',
      },
    ],
  },
}

export default async function ClassPage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params
  const classInfo = classData[id]

  if (!classInfo) {
    return (
      <div className="min-h-screen bg-background">
        <div className="container mx-auto px-6 py-24 md:px-12 lg:px-24">
          <p className="text-lg text-muted-foreground">Class not found</p>
          <Link href="/" className="mt-4 inline-block text-sm underline">
            Return home
          </Link>
        </div>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-background">
      {/* Header */}
      <header className="border-b border-border">
        <div className="container mx-auto px-6 py-8 md:px-12 lg:px-24">
          <Link
            href="/"
            className="inline-flex items-center gap-2 text-sm text-muted-foreground transition-colors hover:text-foreground"
          >
            <ArrowLeft className="h-4 w-4" />
            Back to all classes
          </Link>
        </div>
      </header>

      {/* Class Info */}
      <section className="container mx-auto px-6 py-24 md:px-12 lg:px-24">
        <div className="mb-4">
          <div className="text-sm font-mono text-muted-foreground">{classInfo.code}</div>
        </div>
        <h1 className="text-balance text-5xl font-medium leading-tight tracking-tight text-foreground md:text-7xl">
          {classInfo.name}
        </h1>
        <p className="mt-8 max-w-2xl text-pretty text-lg leading-relaxed text-muted-foreground">
          {classInfo.description}
        </p>
      </section>

      {/* Upload Section */}
      <section className="container mx-auto px-6 pb-16 md:px-12 lg:px-24">
        <Button className="gap-2 " disabled>
          <Upload className="h-4 w-4 " />
          Upload New Cheatsheet
        </Button>
      </section>

      {/* Resources */}
      <section className="container mx-auto px-6 pb-32 md:px-12 lg:px-24">
        <div className="mb-12">
          <h2 className="text-sm font-medium uppercase tracking-wider text-muted-foreground">
            Resources ({classInfo.cheatsheets.length})
          </h2>
        </div>

        {classInfo.cheatsheets.length > 0 ? (
          <div className="grid gap-px bg-border md:grid-cols-2 lg:grid-cols-3">
            {classInfo.cheatsheets.map((sheet) => (
              <div key={sheet.id} className="group bg-background p-8 transition-colors hover:bg-muted">
                <div className="flex flex-col gap-4">
                  <div className="flex items-start justify-between gap-4">
                    {sheet.type === 'pdf' ? (
                      <FileText className="h-5 w-5 flex-shrink-0 text-foreground" />
                    ) : (
                      <ExternalLink className="h-5 w-5 flex-shrink-0 text-foreground" />
                    )}
                    <div className="text-xs font-mono text-muted-foreground">{sheet.type.toUpperCase()}</div>
                  </div>

                  <div className="space-y-2">
                    <h3 className="text-balance text-lg font-medium leading-tight text-foreground">{sheet.title}</h3>
                    {sheet.uploadDate && (
                      <p className="text-xs text-muted-foreground">
                        Added{' '}
                        {new Date(sheet.uploadDate).toLocaleDateString('en-US', {
                          year: 'numeric',
                          month: 'short',
                          day: 'numeric',
                        })}
                      </p>
                    )}
                  </div>

                  {sheet.type === 'external' && sheet.url && (
                    <a
                      href={sheet.url}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="mt-2 inline-flex items-center gap-2 text-sm text-foreground underline transition-colors hover:text-muted-foreground"
                    >
                      Visit resource
                      <ArrowRight className="h-3 w-3" />
                    </a>
                  )}

                  {sheet.type === 'pdf' && (
                    <a
                      href={sheet.url}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="mt-2 inline-flex items-center gap-2 text-sm text-foreground underline transition-colors hover:text-muted-foreground"
                    >
                      View PDF
                      <ArrowRight className="h-3 w-3" />
                    </a>
                  )}
                </div>
              </div>
            ))}
          </div>
        ) : (
          <div className="rounded-sm border border-border bg-muted/30 p-16 text-center">
            <p className="text-muted-foreground">No cheatsheets uploaded yet. Be the first to contribute!</p>
          </div>
        )}
      </section>

      {/* Footer */}
      <footer className="border-t border-border">
        <div className="container mx-auto px-6 py-12 md:px-12 lg:px-24">
          <p className="text-sm text-muted-foreground">
            © {new Date().getFullYear()} Michaels Sheets. All materials for educational purposes.
          </p>
        </div>
      </footer>
    </div>
  )
}
