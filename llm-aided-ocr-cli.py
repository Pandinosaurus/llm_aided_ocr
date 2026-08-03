import argparse
import asyncio
from llm_aided_ocr import main as process_pdf


def parse_arguments():
    parser = argparse.ArgumentParser(description="Process a PDF file with OCR and LLM correction.")
    parser.add_argument("input_file", help="Path to the input PDF file")
    parser.add_argument("--max-pages", type=int, default=0, help="Maximum number of pages to process (0 for all pages)")
    parser.add_argument("--skip-pages", type=int, default=0, help="Number of pages to skip from the beginning")
    parser.add_argument("--no-markdown", action="store_true", help="Don't reformat the output as markdown")
    parser.add_argument("--keep-headers", action="store_true", help="Keep headers and page numbers in the corrected output")
    return parser.parse_args()

async def run_pdf_processor(args):
    await process_pdf(
        input_pdf_file_path=args.input_file,
        max_test_pages=args.max_pages,
        skip_first_n_pages=args.skip_pages,
        reformat_as_markdown=not args.no_markdown,
        suppress_headers_and_page_numbers=not args.keep_headers,
    )

if __name__ == "__main__":
    args = parse_arguments()
    asyncio.run(run_pdf_processor(args))
