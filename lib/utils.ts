import { clsx, type ClassValue } from 'clsx'
import { twMerge } from 'tailwind-merge'

// start?
export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}
