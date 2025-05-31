task_sample_webapp = """
### Webapp Form Filler Test Agent

**Objective:**
Visit local webapp and fill the form.

### Step 1: Navigate to the Website
- Open [localhost:3000](https://localhost:3000).

---

### Step 2: Fill the form

#### Form Data:

- Fill the form with the following data:
    - Name: paresh
    - Email: test@test.com
    - Phone: 1234567890
    - Message: test message

---

### Step 3: Submit the form

- Submit the form by clicking the submit button.

---

### Step 4: Check the response

- Check the response in the modal.

---

### Step 5: Close the modal

- Close the modal if it's open by clicking the close button.
- Verify that the modal is closed.

---

### Step 6: Verify the form

- Verify that the form is back to default state after the modal is closed.

---

### Step 7: Output Response

If all the steps are completed successfully, output the following:

"Test passed successfully"

If any step fails, output the following:

"Test failed"

---

**Important:** Ensure efficiency and accuracy throughout the process."""