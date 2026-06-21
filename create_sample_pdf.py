"""
Helper script to create a sample PDF for testing the RAG pipeline.
Run this once to generate sample.pdf in the data/documents folder.
"""

try:
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas
    from reportlab.lib.units import inch
    
    # Create PDF
    pdf_path = "data/documents/sample.pdf"
    c = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter
    
    # Add title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(1*inch, height - 1*inch, "Company Approval Process")
    
    # Add content
    c.setFont("Helvetica", 12)
    y = height - 1.5*inch
    
    content = [
        "1. Request Submission",
        "   - Submit approval request with required documentation",
        "   - Include justification and business case",
        "",
        "2. Manager Review",
        "   - Manager evaluates request within 3 business days",
        "   - Provides feedback or approves",
        "",
        "3. Director Approval",
        "   - Director reviews manager recommendation",
        "   - Makes final decision",
        "",
        "4. Finance Verification",
        "   - Finance verifies budget allocation",
        "   - Confirms funding availability",
        "",
        "5. Notification",
        "   - Requestor is notified of decision",
        "   - Approval documentation is archived"
    ]
    
    for line in content:
        c.drawString(1*inch, y, line)
        y -= 0.2*inch
    
    c.save()
    print(f"✓ Sample PDF created at {pdf_path}")
    
except ImportError:
    print("reportlab not installed. Installing...")
    import subprocess
    subprocess.check_call(["pip", "install", "reportlab"])
    print("Please run this script again.")
