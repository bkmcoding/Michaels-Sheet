import Link from "next/link"
import { ArrowRight } from "lucide-react"

const classes = [
  {
    id: "data-structures",
    name: "Data Structures",
    code: "CS 201",
    description: "Comprehensive notes on algorithms, trees, graphs, and complexity analysis",
  },
  {
    id: "machine-learning",
    name: "Machine Learning",
    code: "CS 405",
    description: "Neural networks, optimization, and model evaluation frameworks",
  },
  {
    id: "linear-algebra",
    name: "Linear Algebra",
    code: "MATH 251",
    description: "Vector spaces, transformations, eigenvalues and matrix operations",
  },
  {
    id: "cybersecurity",
    name: "Cybersecurity",
    code: "CS 450",
    description: "Network security, cryptography, penetration testing and threat analysis",
  },
  {
    id: "calc-iii",
    name: "Calculus III",
    code: "MATH 253",
    description: "Multivariable calculus, partial derivatives, and vector calculus",
  },
]

export default function HomePage() {
  return (
    <div className="min-h-screen bg-background">
      {/* Header */}
      <header className="border-b border-border">
        <div className="container mx-auto px-6 py-8 md:px-12 lg:px-24">
          <h1 className="text-2xl font-medium tracking-tight text-foreground">Cheatsheets</h1>
        </div>
      </header>

      {/* Hero Section */}
      <section className="container mx-auto px-6 py-24 md:px-12 md:py-32 lg:px-24 lg:py-40">
        <div className="max-w-4xl">
          <h2 className="text-balance text-5xl font-medium leading-tight tracking-tight text-foreground md:text-7xl lg:text-8xl">
            Your academic resource hub.
          </h2>
          <p className="mt-8 max-w-2xl text-pretty text-lg leading-relaxed text-muted-foreground md:text-xl">
            Organized cheatsheets, PDFs, and external resources for all your classes. Everything in one place,
            accessible anytime.
          </p>
        </div>
      </section>

      {/* Classes Grid */}
      <section className="container mx-auto px-6 pb-32 md:px-12 lg:px-24">
        <div className="mb-16">
          <h3 className="text-sm font-medium uppercase tracking-wider text-muted-foreground">Browse Classes</h3>
        </div>

        <div className="grid gap-px bg-border md:grid-cols-2">
          {classes.map((classItem) => (
            <Link
              key={classItem.id}
              href={`/class/${classItem.id}`}
              className="group bg-background p-12 transition-colors hover:bg-muted"
            >
              <div className="flex items-start justify-between gap-8">
                <div className="flex-1 space-y-4">
                  <div className="space-y-1">
                    <div className="text-sm font-mono text-muted-foreground">{classItem.code}</div>
                    <h4 className="text-2xl font-medium tracking-tight text-foreground">{classItem.name}</h4>
                  </div>
                  <p className="text-pretty text-sm leading-relaxed text-muted-foreground">{classItem.description}</p>
                </div>
                <ArrowRight className="h-5 w-5 flex-shrink-0 text-foreground transition-transform group-hover:translate-x-1" />
              </div>
            </Link>
          ))}
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t border-border">
        <div className="container mx-auto px-6 py-12 md:px-12 lg:px-24">
          <p className="text-sm text-muted-foreground">
            © {new Date().getFullYear()} Cheatsheets. All materials for educational purposes.
          </p>
        </div>
      </footer>
    </div>
  )
}
